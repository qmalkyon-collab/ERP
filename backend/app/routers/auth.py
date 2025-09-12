from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from ..db import get_session
from ..models import User
from ..schemas import LoginForm, Token, UserCreate, UserOut
from ..security import verify_password, get_password_hash, create_access_token
from ..config import settings

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserOut)
def register(payload: UserCreate, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.email == payload.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(
        email=payload.email,
        full_name=payload.full_name,
        hashed_password=get_password_hash(payload.password),
        tenant_id=payload.tenant_id,
        role="manager" if payload.email.endswith("@yourcompany.com") else "user",
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.post("/login", response_model=Token)
def login(form: LoginForm, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == form.username)).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token({"sub": user.email, "tenant": user.tenant_id, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}