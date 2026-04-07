import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.data.db import Base
from app.data.db import get_db as real_get_db
from app.core.auth import hash_password

from app.models.user_models import User


from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    app.dependency_overrides[real_get_db] = override_get_db

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()


def seed_admin_and_user():
    "Create admin + normal user in test DB and return nothing (data lives in DB)."
    db = TestingSessionLocal()

    admin = User(
        username="admin",
        hashed_password=hash_password("admin123"),
        is_admin=True
    )
    user = User(
        username="user1",
        hashed_password=hash_password("pass123"),
        is_admin=False
    )
    db.add(admin)
    db.add(user)
    db.commit()
    db.close()


def login(client, username, password):
    res = client.post("/ubl/auth/login", json={"username": username, "password": password})
    return res


def test_register_user_success(client):
    res = client.post("/ubl/auth/register", json={"username": "newuser", "password": "pw123"})
    assert res.status_code == 200
    assert res.json() == {"message": "User registered"}


def test_register_user_duplicate_username(client):
    client.post("/ubl/auth/register", json={"username": "dup", "password": "pw123"})
    res = client.post("/ubl/auth/register", json={"username": "dup", "password": "pw123"})
    assert res.status_code == 400
    assert "Username already exists" in str(res.json())


def test_login_success_returns_token(client):
    seed_admin_and_user()

    res = login(client, "user1", "pass123")
    assert res.status_code == 200

    data = res.json()
    assert "access_token" in data
    assert "token_type" in data
    assert data["token_type"] == "bearer"


def test_login_invalid_credentials(client):
    seed_admin_and_user()

    res = login(client, "user1", "wrongpw")
    assert res.status_code == 401
    assert res.json()["detail"] == "Invalid credentials"


def test_me_requires_auth(client):
    res = client.get("/ubl/auth/me")
    assert res.status_code in [401, 403]


def test_me_success_with_token(client):
    seed_admin_and_user()

    res = login(client, "user1", "pass123")
    token = res.json()["access_token"]

    res2 = client.get("/ubl/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert res2.status_code == 200
    assert res2.json()["username"] == "user1"


def test_admin_list_users_forbidden_for_normal_user(client):
    seed_admin_and_user()

    res = login(client, "user1", "pass123")
    token = res.json()["access_token"]

    res2 = client.get("/ubl/auth/admin/list-users", headers={"Authorization": f"Bearer {token}"})
    assert res2.status_code == 403
    assert res2.json()["detail"] == "Admin access required"


def test_admin_list_users_success_for_admin(client):
    seed_admin_and_user()

    res = login(client, "admin", "admin123")
    token = res.json()["access_token"]

    res2 = client.get("/ubl/auth/admin/list-users", headers={"Authorization": f"Bearer {token}"})
    assert res2.status_code == 200
    users = res2.json()
    assert isinstance(users, list)
    assert any(u["username"] == "admin" for u in users)


def test_admin_delete_user(client):
    seed_admin_and_user()

    admin_login = login(client, "admin", "admin123")
    admin_token = admin_login.json()["access_token"]


    users_res = client.get("/ubl/auth/admin/list-users", headers={"Authorization": f"Bearer {admin_token}"})
    user1 = None
    for u in users_res.json():
        if u["username"] == "user1":
            user1 = u
            break
    assert user1 is not None

    del_res = client.delete(f"/ubl/auth/admin/delete/{user1['id']}", headers={"Authorization": f"Bearer {admin_token}"})
    assert del_res.status_code == 200 or del_res.status_code == 204

    del_res2 = client.delete(f"/ubl/auth/admin/delete/{user1['id']}", headers={"Authorization": f"Bearer {admin_token}"})
    assert del_res2.status_code == 404


def test_logout(client):
    res = client.post("/ubl/auth/logout")
    assert res.status_code == 200
    assert res.json() == {"message": "Logout successful"}

def test_admin_list_users_includes_despatch(client):
    seed_admin_and_user()

    res = login(client, "admin", "admin123")
    token = res.json()["access_token"]

    res2 = client.get(
        "/ubl/auth/admin/list-users",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert res2.status_code == 200

    users = res2.json()
    assert isinstance(users, list)
    assert any(u["username"] == "admin" for u in users)

    first_user = users[0]
    assert "despatches" in first_user
    assert isinstance(first_user["despatches"], list)

def test_login_unknown_username(client):
    seed_admin_and_user()

    res = login(client, "ghost", "whatever")
    assert res.status_code == 401
    assert res.json()["detail"] == "Invalid credentials"


def test_admin_delete_nonexistent_user(client):
    seed_admin_and_user()

    admin_login = login(client, "admin", "admin123")
    admin_token = admin_login.json()["access_token"]

    res = client.delete(
        "/ubl/auth/admin/delete/9999",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert res.status_code == 404
    assert res.json()["detail"] == "User not found"


def test_admin_delete_user_forbidden_for_normal_user(client):
    seed_admin_and_user()

    user_login = login(client, "user1", "pass123")
    user_token = user_login.json()["access_token"]

    res = client.delete(
        "/ubl/auth/admin/delete/1",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert res.status_code == 403
    assert res.json()["detail"] == "Admin access required"


def test_me_success_returns_id_and_username(client):
    seed_admin_and_user()

    res = login(client, "user1", "pass123")
    token = res.json()["access_token"]

    res2 = client.get(
        "/ubl/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res2.status_code == 200
    data = res2.json()
    assert "id" in data
    assert data["username"] == "user1"


def test_admin_list_users_includes_expected_fields(client):
    seed_admin_and_user()

    res = login(client, "admin", "admin123")
    token = res.json()["access_token"]

    res2 = client.get(
        "/ubl/auth/admin/list-users",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert res2.status_code == 200
    users = res2.json()

    first_user = users[0]
    assert "id" in first_user
    assert "username" in first_user
    assert "is_admin" in first_user
    assert "despatches" in first_user
    assert isinstance(first_user["despatches"], list)