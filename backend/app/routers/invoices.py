from fastapi import APIRouter

router = APIRouter(prefix="/invoices", tags=["invoices"])

@router.get("/")
def placeholder():
    return {"message": "TODO: implement invoices"}