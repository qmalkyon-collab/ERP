from fastapi import APIRouter

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("/")
def placeholder():
    return {"message": "TODO: implement customers"}