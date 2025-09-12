from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import Session, select
from ..deps import get_db, get_current_user, require_role
from ..models import Product
from ..schemas import ProductCreate, ProductOut

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[ProductOut])
def list_products(session: Session = Depends(get_db), user=Depends(get_current_user)):
    return session.exec(select(Product).where(Product.tenant_id == user.tenant_id)).all()

@router.post("/", response_model=ProductOut)
def create_product(payload: ProductCreate, session: Session = Depends(get_db), user=Depends(require_role("admin", "manager"))):
    existing = session.exec(select(Product).where(Product.sku == payload.sku)).first()
    if existing:
        raise HTTPException(status_code=400, detail="SKU already exists")
    product = Product(**payload.dict())
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, session: Session = Depends(get_db), user=Depends(get_current_user)):
    product = session.get(Product, product_id)
    if not product or product.tenant_id != user.tenant_id:
        raise HTTPException(status_code=404, detail="Not found")
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int, session: Session = Depends(get_db), user=Depends(require_role("admin"))):
    product = session.get(Product, product_id)
    if not product or product.tenant_id != user.tenant_id:
        raise HTTPException(status_code=404, detail="Not found")
    session.delete(product)
    session.commit()
    return {"status": "ok"}