from sqlalchemy import Boolean, Column, Integer, String, Double

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, default="dude")
    wallet = Column(Double, default=0)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
