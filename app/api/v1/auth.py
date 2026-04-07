from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.data.db import get_db
from app.models.user_models import User, RegisterRequest, LoginRequest, TokenResponse, Despatch
from app.core.auth import hash_password, verify_password, create_token, get_current_user, admin_required

router = APIRouter(tags=["auth"])

# Register a new user
@router.post("/register")
def register_user(user: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(400, "Username already exists")

    new_user = User(
        username=user.username,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "User registered"}


# Login an existing user
@router.post("/login", response_model=TokenResponse)
def login_user(request: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user.id)
    return {"access_token": token}


# Return a list of all users
@router.get("/admin/list-users")
def list_all_users(
    db: Session = Depends(get_db),
    admin: User = Depends(admin_required)
):
    users = db.query(User).all()

    result = []
    for u in users:
        despatches = db.query(Despatch).filter(Despatch.user_id == u.id).all()

        result.append({
            "id": u.id,
            "username": u.username,
            "is_admin": u.is_admin,
            "despatches": [
                {
                    "uuid": d.uuid,
                    "despatch_id": d.despatch_id
                }
                for d in despatches
            ]
        })

    return result


# Deletes a user from the database
@router.delete("/admin/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), admin: User = Depends(admin_required)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()


# Logout a user
@router.post("/logout")
def logout_user():
    return {"message": "Logout successful"}


# Returns the current user
@router.get("/me")
def get_user(user: User = Depends(get_current_user)):
    return {"id": user.id, "username": user.username}

# # Wipes all users
# @router.delete("/admin/wipe-users")
# def wipe_users(
#     confirm: str,
#     db: Session = Depends(get_db),
#     admin: User = Depends(admin_required)
# ):
#     if confirm != "DELETE_ALL_USERS":
#         raise HTTPException(
#             status_code=400,
#             detail="Confirmation string required: DELETE_ALL_USERS"
#         )

#     deleted = db.query(User).delete()
#     db.commit()

#     return {
#         "message": "All users deleted",
#         "deleted_count": deleted
#     }