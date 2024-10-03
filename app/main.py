from fastapi import FastAPI

from app.api.endpoints import user, flag

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(flag.router, prefix="/flags", tags=["flags"])
