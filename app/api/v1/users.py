from fastapi import APIRouter, Depends
from fishauth.models.user import User
from sqlalchemy.orm import Session
from app import deps

router = APIRouter()


@router.get("/")
async def get_users():
    return {"message": "Users!"}


@router.get("/user")
async def read_all_by_user(db: Session = Depends(deps.get_db)):
    return db.query(User).all()
