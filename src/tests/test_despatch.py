import pytest
from fastapi.testclient import TestClient
from fastapi.routing import APIRoute
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.data.db import get_db
from app.core.auth import get_current_user
from app.models.user_models import User, Despatch, Base

API_PREFIX = "/ubl/v3/despatch-advice"

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def override_user(user):
    def _override():
        return user
    return _override


def get_route_path(path_suffix: str, method: str) -> str:
    target_path = f"{API_PREFIX}{path_suffix}"

    for route in app.routes:
        if isinstance(route, APIRoute):
            route_methods = route.methods or set()
            if method.upper() in route_methods and route.path == target_path:
                return route.path

    raise AssertionError(f"Could not find exact route '{target_path}' for method {method}")


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture
def normal_user(db_session):
    user = User(
        username="user1",
        hashed_password="hashed_password",
        is_admin=False
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


@pytest.fixture
def admin_user(db_session):
    user = User(
        username="admin1",
        hashed_password="hashed_password",
        is_admin=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def test_generate_despatch_success(client, db_session, normal_user, monkeypatch):
    from app.api.v1 import despatch as despatch_module

    app.dependency_overrides[get_current_user] = override_user(normal_user)

    def fake_parse_ubl_order(xml_text):
        return {"order_id": "ORDER123"}

    def fake_generate_despatch_advice(order_data, carrier, dispatch_date, notes):
        assert order_data == {"order_id": "ORDER123"}
        assert carrier == "DHL"
        assert dispatch_date == "2026-04-07"
        assert notes == "fragile"
        return "<DespatchAdvice>generated</DespatchAdvice>"

    monkeypatch.setattr(despatch_module, "parse_ubl_order", fake_parse_ubl_order)
    monkeypatch.setattr(despatch_module, "generate_despatch_advice", fake_generate_despatch_advice)

    response = client.post(
        get_route_path("/generate", "POST"),
        files={"order_xml": ("order.xml", b"<Order>abc</Order>", "application/xml")},
        data={
            "carrier": "DHL",
            "dispatch_date": "2026-04-07",
            "notes": "fragile"
        }
    )

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/xml")
    assert "Despatch-UUID" in response.headers
    assert 'attachment; filename="Despatch_ORDER123_' in response.headers["content-disposition"]
    assert response.text == "<DespatchAdvice>generated</DespatchAdvice>"

    saved = db_session.query(Despatch).filter(Despatch.despatch_id == "ORDER123").first()
    assert saved is not None
    assert saved.user_id == normal_user.id
    assert saved.xml_content == "<DespatchAdvice>generated</DespatchAdvice>"


def test_generate_despatch_empty_uploaded_file(client, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    response = client.post(
        get_route_path("/generate", "POST"),
        files={"order_xml": ("order.xml", b"", "application/xml")},
        data={
            "carrier": "",
            "dispatch_date": "",
            "notes": ""
        }
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Empty uploaded file"


def test_generate_despatch_invalid_xml_returns_422(client, normal_user, monkeypatch):
    from app.api.v1 import despatch as despatch_module

    app.dependency_overrides[get_current_user] = override_user(normal_user)

    def fake_parse_ubl_order(xml_text):
        raise ValueError("Invalid UBL Order XML")

    monkeypatch.setattr(despatch_module, "parse_ubl_order", fake_parse_ubl_order)

    response = client.post(
        get_route_path("/generate", "POST"),
        files={"order_xml": ("order.xml", b"<bad>", "application/xml")},
        data={
            "carrier": "",
            "dispatch_date": "",
            "notes": ""
        }
    )

    assert response.status_code == 422
    assert response.json()["detail"] == "Invalid UBL Order XML"


def test_generate_despatch_generator_failure_returns_500(client, normal_user, monkeypatch):
    from app.api.v1 import despatch as despatch_module

    app.dependency_overrides[get_current_user] = override_user(normal_user)

    def fake_parse_ubl_order(xml_text):
        return {"order_id": "ORDER123"}

    def fake_generate_despatch_advice(order_data, carrier, dispatch_date, notes):
        raise Exception("Generation failed")

    monkeypatch.setattr(despatch_module, "parse_ubl_order", fake_parse_ubl_order)
    monkeypatch.setattr(despatch_module, "generate_despatch_advice", fake_generate_despatch_advice)

    response = client.post(
        get_route_path("/generate", "POST"),
        files={"order_xml": ("order.xml", b"<Order></Order>", "application/xml")},
        data={
            "carrier": "",
            "dispatch_date": "",
            "notes": ""
        }
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "Generation failed"


def test_list_despatches_returns_only_current_users_files(client, db_session, normal_user, admin_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    mine = Despatch(
        uuid="uuid-1",
        despatch_id="D001",
        xml_content="<xml>mine</xml>",
        user_id=normal_user.id
    )
    not_mine = Despatch(
        uuid="uuid-2",
        despatch_id="D002",
        xml_content="<xml>other</xml>",
        user_id=admin_user.id
    )

    db_session.add_all([mine, not_mine])
    db_session.commit()

    response = client.get(get_route_path("/list", "GET"))

    assert response.status_code == 200
    assert response.json() == [
        {
            "uuid": "uuid-1",
            "despatch_id": "D001"
        }
    ]


def test_admin_list_all_despatches_success(client, db_session, admin_user, normal_user):
    app.dependency_overrides[get_current_user] = override_user(admin_user)

    d1 = Despatch(uuid="u1", despatch_id="D001", xml_content="<xml>1</xml>", user_id=normal_user.id)
    d2 = Despatch(uuid="u2", despatch_id="D002", xml_content="<xml>2</xml>", user_id=admin_user.id)

    db_session.add_all([d1, d2])
    db_session.commit()

    response = client.get(get_route_path("/admin/list", "GET"))

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 2
    assert data[0]["uuid"] == "u1"
    assert data[0]["despatch_id"] == "D001"
    assert data[0]["user_id"] == normal_user.id
    assert data[1]["uuid"] == "u2"
    assert data[1]["despatch_id"] == "D002"
    assert data[1]["user_id"] == admin_user.id


def test_admin_list_all_despatches_forbidden_for_non_admin(client, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    response = client.get(get_route_path("/admin/list", "GET"))

    assert response.status_code == 403
    assert response.json()["detail"] == "Admin access required"


def test_get_despatch_by_id_owner_success(client, db_session, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="uuid-1",
        despatch_id="D100",
        xml_content="<xml>mine</xml>",
        user_id=normal_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/id/{id}", "GET").replace("{id}", "D100"))

    assert response.status_code == 200
    assert response.text == "<xml>mine</xml>"
    assert response.headers["Despatch-ID"] == "D100"
    assert response.headers["Despatch-UUID"] == "uuid-1"
    assert response.headers["content-type"].startswith("application/xml")


def test_get_despatch_by_id_admin_success(client, db_session, admin_user, normal_user):
    app.dependency_overrides[get_current_user] = override_user(admin_user)

    d = Despatch(
        uuid="uuid-2",
        despatch_id="D200",
        xml_content="<xml>user-file</xml>",
        user_id=normal_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/id/{id}", "GET").replace("{id}", "D200"))

    assert response.status_code == 200
    assert response.text == "<xml>user-file</xml>"


def test_get_despatch_by_id_not_found(client, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    response = client.get(get_route_path("/id/{id}", "GET").replace("{id}", "NOPE"))

    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_get_despatch_by_id_forbidden(client, db_session, normal_user, admin_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="uuid-3",
        despatch_id="D300",
        xml_content="<xml>not yours</xml>",
        user_id=admin_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/id/{id}", "GET").replace("{id}", "D300"))

    assert response.status_code == 403
    assert response.json()["detail"] == "Not allowed"


def test_get_despatch_by_uuid_owner_success(client, db_session, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="abc-123",
        despatch_id="D400",
        xml_content="<xml>mine</xml>",
        user_id=normal_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/uuid/{uuid}", "GET").replace("{uuid}", "abc-123"))

    assert response.status_code == 200
    assert response.text == "<xml>mine</xml>"
    assert response.headers["Despatch-ID"] == "D400"
    assert response.headers["Despatch-UUID"] == "abc-123"


def test_get_despatch_by_uuid_admin_success(client, db_session, admin_user, normal_user):
    app.dependency_overrides[get_current_user] = override_user(admin_user)

    d = Despatch(
        uuid="abc-456",
        despatch_id="D500",
        xml_content="<xml>other</xml>",
        user_id=normal_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/uuid/{uuid}", "GET").replace("{uuid}", "abc-456"))

    assert response.status_code == 200
    assert response.text == "<xml>other</xml>"


def test_get_despatch_by_uuid_not_found(client, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    response = client.get(get_route_path("/uuid/{uuid}", "GET").replace("{uuid}", "missing-uuid"))

    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_get_despatch_by_uuid_forbidden(client, db_session, normal_user, admin_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="abc-789",
        despatch_id="D600",
        xml_content="<xml>other</xml>",
        user_id=admin_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/uuid/{uuid}", "GET").replace("{uuid}", "abc-789"))

    assert response.status_code == 403
    assert response.json()["detail"] == "Not allowed"


def test_download_despatch_by_id_owner_success(client, db_session, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="uuid-10",
        despatch_id="D700",
        xml_content="<xml>download me</xml>",
        user_id=normal_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/id/download/{id}", "GET").replace("{id}", "D700"))

    assert response.status_code == 200
    assert response.text == "<xml>download me</xml>"
    assert response.headers["content-type"].startswith("application/xml")
    assert response.headers["content-disposition"] == 'attachment; filename="Despatch_D700.xml"'


def test_download_despatch_by_id_admin_success(client, db_session, admin_user, normal_user):
    app.dependency_overrides[get_current_user] = override_user(admin_user)

    d = Despatch(
        uuid="uuid-11",
        despatch_id="D701",
        xml_content="<xml>other</xml>",
        user_id=normal_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/id/download/{id}", "GET").replace("{id}", "D701"))

    assert response.status_code == 200
    assert response.text == "<xml>other</xml>"


def test_download_despatch_by_id_not_found(client, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    response = client.get(get_route_path("/id/download/{id}", "GET").replace("{id}", "MISSING"))

    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_download_despatch_by_id_forbidden(client, db_session, normal_user, admin_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="uuid-12",
        despatch_id="D702",
        xml_content="<xml>other</xml>",
        user_id=admin_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/id/download/{id}", "GET").replace("{id}", "D702"))

    assert response.status_code == 403
    assert response.json()["detail"] == "Not allowed"


def test_download_despatch_by_uuid_owner_success(client, db_session, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="uuid-download",
        despatch_id="D800",
        xml_content="<xml>download me</xml>",
        user_id=normal_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/uuid/download/{uuid}", "GET").replace("{uuid}", "uuid-download"))

    assert response.status_code == 200
    assert response.text == "<xml>download me</xml>"
    assert response.headers["content-disposition"] == 'attachment; filename="Despatch_uuid-download.xml"'


def test_download_despatch_by_uuid_not_found(client, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    response = client.get(get_route_path("/uuid/download/{uuid}", "GET").replace("{uuid}", "missing-uuid"))

    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_download_despatch_by_uuid_forbidden(client, db_session, normal_user, admin_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="forbidden-uuid",
        despatch_id="D801",
        xml_content="<xml>other</xml>",
        user_id=admin_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.get(get_route_path("/uuid/download/{uuid}", "GET").replace("{uuid}", "forbidden-uuid"))

    assert response.status_code == 403
    assert response.json()["detail"] == "Not allowed"


def test_delete_despatch_by_id_owner_success(client, db_session, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="uuid-delete",
        despatch_id="D900",
        xml_content="<xml>delete me</xml>",
        user_id=normal_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.delete(get_route_path("/id/{id}", "DELETE").replace("{id}", "D900"))

    assert response.status_code == 200
    assert response.json() == {"message": "Deleted successfully"}

    deleted = db_session.query(Despatch).filter(Despatch.despatch_id == "D900").first()
    assert deleted is None


def test_delete_despatch_by_id_admin_success(client, db_session, admin_user, normal_user):
    app.dependency_overrides[get_current_user] = override_user(admin_user)

    d = Despatch(
        uuid="uuid-delete-admin",
        despatch_id="D901",
        xml_content="<xml>delete me</xml>",
        user_id=normal_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.delete(get_route_path("/id/{id}", "DELETE").replace("{id}", "D901"))

    assert response.status_code == 200
    assert response.json() == {"message": "Deleted successfully"}

    deleted = db_session.query(Despatch).filter(Despatch.despatch_id == "D901").first()
    assert deleted is None


def test_delete_despatch_by_id_not_found(client, normal_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    response = client.delete(get_route_path("/id/{id}", "DELETE").replace("{id}", "NOPE"))

    assert response.status_code == 404
    assert response.json()["detail"] == "Not found"


def test_delete_despatch_by_id_forbidden(client, db_session, normal_user, admin_user):
    app.dependency_overrides[get_current_user] = override_user(normal_user)

    d = Despatch(
        uuid="uuid-forbidden",
        despatch_id="D902",
        xml_content="<xml>other</xml>",
        user_id=admin_user.id
    )
    db_session.add(d)
    db_session.commit()

    response = client.delete(get_route_path("/id/{id}", "DELETE").replace("{id}", "D902"))

    assert response.status_code == 403
    assert response.json()["detail"] == "Not allowed"