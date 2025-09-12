from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from .db import get_session
from .security import oauth2_scheme
from .config import settings
from .models import User
import jwt

def get_db():
    yield from get_session()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, settings.APP_SECRET, algorithms=["HS256"])
        sub = payload.get("sub")
        if not sub:
            raise ValueError("Invalid token")
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    user = db.exec(select(User).where(User.email == sub)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user

def require_role(*roles: str):
    def wrapper(user: User = Depends(get_current_user)):
        if user.role not in roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return wrapper