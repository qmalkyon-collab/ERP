from fastapi import APIRouter

router = APIRouter(prefix="/sales", tags=["sales"])

@router.get("/")
def placeholder():
    return {"message": "TODO: implement sales"}