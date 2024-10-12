from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app import schemas, crud

router = APIRouter()

from app.api.dependencies import get_db


@router.post("/reg/", response_model=schemas.User)
def create_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, user_name=username)
    if db_user:
        raise HTTPException(status_code=400, detail="Name already registered")
    return crud.create_user(db=db, user_name=username)


@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}")
def update_user_wallet(user_id: int, wallet: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    crud.update_user_wallet(db, user_id=user_id, wallet=wallet)
    return {"message": "User updated"}


@router.get("/score/", response_model=List[schemas.UserScore])
def get_user_score(db: Session = Depends(get_db)):
    scores = crud.get_user_score(db)
    return scores
