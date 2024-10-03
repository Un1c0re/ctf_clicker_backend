from sqlalchemy.orm import Session

from ..core.security import hash_password
from ..models.user import User
from ..schemas.user import UserCreate, UserScore


def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def update_user_wallet(db: Session, user_id: int, wallet: float):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.wallet = wallet
    db.commit()
    db.refresh(db_user)


def get_user_score(db: Session):
    users = db.query(User).order_by(User.wallet.desc()).all()
    return [UserScore(id=user.id, name=user.name, score=user.wallet) for user in users]
