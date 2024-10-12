from sqlalchemy.orm import Session

from ..models.user import User
from ..schemas.user import UserScore


def create_user(db: Session, user_name: str):
    db_user = User(name=user_name, wallet=0)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_name(db: Session, user_name: str):
    return db.query(User).filter(User.name == user_name).first()


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
