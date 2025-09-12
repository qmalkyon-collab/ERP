from typing import Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginForm(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    email: str
    full_name: Optional[str] = None
    password: str
    tenant_id: str = "default"

class UserOut(BaseModel):
    id: int
    email: str
    full_name: Optional[str] = None
    role: str
    tenant_id: str
    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    unit_price: float
    tenant_id: str = "default"

class ProductOut(BaseModel):
    id: int
    sku: str
    name: str
    description: Optional[str] = None
    unit_price: float
    is_active: bool
    tenant_id: str
    class Config:
        from_attributes = True