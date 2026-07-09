# scripts/bootstrap_super_admin.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db.database import SessionLocal
from src.models.user import User
from src.core.security import hash_password

EMAIL = "mhmdkhyry067@gmail.com"          # change this
PASSWORD = "123456789"   # change this
FULL_NAME = "System Administrator"

db = SessionLocal()
existing = db.query(User).filter(User.email == EMAIL).first()
if existing:
    print(f"User {EMAIL} already exists (role={existing.role}). Nothing to do.")
else:
    user = User(
        email=EMAIL,
        hashed_password=hash_password(PASSWORD),
        full_name=FULL_NAME,
        role="super_admin",
        is_active=True,
        student_id=None,
        organization_id=None,
    )
    db.add(user)
    db.commit()
    print(f"super_admin created: {EMAIL}")
db.close()