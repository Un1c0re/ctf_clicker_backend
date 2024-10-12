from sqlalchemy import Column, Integer, String, Double

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, default="dude")
    wallet = Column(Double, default=0)
