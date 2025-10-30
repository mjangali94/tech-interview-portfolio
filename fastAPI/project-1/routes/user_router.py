from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import schemas.user
from schemas.user import UserCreate
from models.user import User
from utils import hashing as hasher
from utils.token import create_access_token
from database import get_db
router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.user.UserResponse)
async def create_user(user: UserCreate, db:Session=Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash(user.password)
    new_user = User(
        username=user.username,
        name=user.name,
        email=user.email,
        password= user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/", response_model=List[schemas.user.UserResponse])
async def read_users(db:Session=Depends(get_db)):
    return db.query(User).all()

@router.post("/login")
def login(form_data: schemas.user.UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not hasher.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

