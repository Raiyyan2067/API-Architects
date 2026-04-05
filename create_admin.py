from app.data.db import get_db, Base, engine
from app.models.user_models import User
from app.core.auth import hash_password


# Create a new DB session
Base.metadata.create_all(bind=engine)
db = next(get_db())

# Check if admin already exists
admin_user = db.query(User).filter(User.username == "admin").first()
if admin_user:
    print("Admin user already exists!")
else:
    password = "admin123"
    new_admin = User(
        username="admin",
        hashed_password=hash_password(password),
        is_admin=True
    )
    db.add(new_admin)
    db.commit()
    print("Admin user 'admin' created successfully!")