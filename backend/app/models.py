from typing import Optional, List
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class Timestamped(SQLModel):
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class UserBase(SQLModel):
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None
    tenant_id: str = Field(default="default", index=True)

class User(UserBase, Timestamped, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    role: str = Field(default="user", index=True)

class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: str = Field(default="default", index=True)
    name: str = Field(index=True)
    vat_number: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: str = Field(default="default", index=True)
    sku: str = Field(index=True, unique=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    unit_price: float = 0.0
    is_active: bool = True

class Warehouse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: str = Field(default="default", index=True)
    code: str = Field(index=True)
    name: str
    address: Optional[str] = None

class InventoryItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: str = Field(default="default", index=True)
    product_id: int = Field(foreign_key="product.id")
    warehouse_id: int = Field(foreign_key="warehouse.id")
    quantity: float = 0.0

class SalesOrder(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: str = Field(default="default", index=True)
    customer_id: int = Field(foreign_key="customer.id")
    status: str = Field(default="draft", index=True)

class SalesOrderLine(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: str = Field(default="default", index=True)
    order_id: int = Field(foreign_key="salesorder.id")
    product_id: int = Field(foreign_key="product.id")
    quantity: float
    unit_price: float

class Invoice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tenant_id: str = Field(default="default", index=True)
    order_id: int = Field(foreign_key="salesorder.id")
    total_amount: float = 0.0
    status: str = Field(default="unpaid", index=True)