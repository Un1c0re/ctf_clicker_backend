from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"flag": "surctf_12345678"}
