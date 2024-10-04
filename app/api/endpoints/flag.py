from fastapi import APIRouter

from app.config import settings

router = APIRouter()


@router.get("/")
async def root():
    flag = settings.flag
    return {"flag": flag}
