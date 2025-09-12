from fastapi import APIRouter

router = APIRouter(prefix="/warehouses", tags=["warehouses"])

@router.get("/")
def placeholder():
    return {"message": "TODO: implement warehouses"}