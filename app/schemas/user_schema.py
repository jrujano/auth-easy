from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from pydantic import BaseModel, ConfigDict, EmailStr
from pydantic.version import VERSION as PYDANTIC_VERSION

PYDANTIC_V2 = PYDANTIC_VERSION.startswith("2.")

SCHEMA = TypeVar("SCHEMA", bound=BaseModel)

if PYDANTIC_V2:  # pragma: no cover

    def model_dump(model: BaseModel, *args, **kwargs) -> Dict[str, Any]:
        return model.model_dump(*args, **kwargs)  # type: ignore

    def model_validate(schema: Type[SCHEMA], obj: Any, *args, **kwargs) -> SCHEMA:
        return schema.model_validate(obj, *args, **kwargs)  # type: ignore

else:  # pragma: no cover  # type: ignore

    def model_dump(model: BaseModel, *args, **kwargs) -> Dict[str, Any]:
        return model.dict(*args, **kwargs)  # type: ignore

    def model_validate(schema: Type[SCHEMA], obj: Any, *args, **kwargs) -> SCHEMA:
        return schema.from_orm(obj)  # type: ignore


class CreateUpdateDictModel(BaseModel):
    def create_update_dict(self):
        return model_dump(
            self,
            exclude_unset=True,
            exclude={
                "id",
                "is_active",
            },
        )

    def create_update_dict_superuser(self):
        return model_dump(self, exclude_unset=True, exclude={"id"})


class BaseUser(CreateUpdateDictModel):
    """Base User model."""

    id: Optional[int]
    names: Optional[str] = None
    last_name: Optional[str] = None
    mother_last_name: Optional[str] = None
    email: EmailStr
    is_active: bool = True
    # is_superuser: bool = False
    # is_verified: bool = False

    if PYDANTIC_V2:  # pragma: no cover
        model_config = ConfigDict(from_attributes=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True


class BaseUserCreate(CreateUpdateDictModel):
    email: EmailStr
    password: str
    password2: str
    names: str
    last_name: str
    mother_last_name: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class BaseUserUpdate(CreateUpdateDictModel):
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None


class UserInDBSchema(CreateUpdateDictModel):
    id: int
    email: EmailStr
    # password: str
    is_staff: bool = False
    is_active: Optional[int] = True
    is_network: Optional[bool] = False
    organization_id: Optional[int] = None
