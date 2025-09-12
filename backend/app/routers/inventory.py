from fastapi import APIRouter

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/")
def placeholder():
    return {"message": "TODO: implement inventory"}