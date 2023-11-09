from fishauth.models.user import User
from app.crud.base import CRUDBase
from app.schemas import BaseUserCreate


class CRUDUser(CRUDBase[User, BaseUserCreate, BaseUserCreate]):
    pass


user_crud = CRUDUser(User)
