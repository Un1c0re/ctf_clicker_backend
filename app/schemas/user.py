from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    wallet: float

    class Config:
        from_attributes = True


class UserScore(BaseModel):
    id: int
    name: str
    score: float
