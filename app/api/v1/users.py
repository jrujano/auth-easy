from fastapi import APIRouter, Depends, Request, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED
from fishauth.models.user import User
from sqlalchemy.orm import Session
from typing import Any
from fishauth.models.user import User
from app import deps
from app.schemas import BaseUser, BaseUserCreate, UserInDBSchema
from app.exceptions import HandlerExceptions
from app.crud import user_crud

router = APIRouter()


@router.get("/")
async def get_users():
    return {"message": "Users!"}


@router.get("/user")
async def read_all_by_user(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    """
    The function `read_all_by_user` reads multiple user records from the database with optional
    pagination.

    :param db: The `db` parameter is of type `Session` and is used to access the database session. It is
    injected using the `Depends` function from the `fastapi` framework
    :type db: Session
    :param skip: The `skip` parameter is used to specify the number of records to skip before returning
    the results. It is used for pagination purposes, allowing you to retrieve a specific subset of
    records, defaults to 0
    :type skip: int (optional)
    :param limit: The `limit` parameter specifies the maximum number of records to retrieve from the
    database. It determines the number of records that will be returned in the result set, defaults to
    100
    :type limit: int (optional)
    :return: multiple user records from the database.
    """
    # return db.query(User).all()
    return user_crud.get_multi(db, skip=skip, limit=limit)


@router.post("/user", response_model=UserInDBSchema)
def signup(
    user_in: BaseUserCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    The `signup` function handles the creation of a new user by checking for duplicate email, validating
    the password, and creating the user in the database.

    :param user_in: The `user_in` parameter is of type `BaseUserCreate`, which is a Pydantic model
    representing the data required to create a new user. It contains fields such as `email`, `password`,
    and `password2` (confirmation password)
    :type user_in: BaseUserCreate
    :param db: The `db` parameter is of type `Session` and is used to access the database session. It is
    obtained using the `get_db` dependency function from the `deps` module
    :type db: Session
    :return: an instance of the `UserInDBSchema` model.
    """
    validation1 = db.query(User).filter(User.email == user_in.email).first()
    if user_in.password != user_in.password2:
        HandlerExceptions.InvalidCredentialsException()

    if validation1 is not None:
        HandlerExceptions.DuplicateEmailException()

    del user_in.password2

    user = user_crud.create(db, obj_in=user_in)

    return user
