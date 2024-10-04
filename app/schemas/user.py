from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    name: str
    wallet: float

    class Config:
        from_attributes = True


class UserScore(BaseModel):
    id: int
    name: str
    score: float
