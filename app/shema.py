import pydantic
from typing import Optional, Type
from abc import ABC

class AbstractUser(pydantic.BaseModel, ABC):
    name: str
    password: str
    email: str

    @pydantic.field_validator("name")
    @classmethod
    def name_length(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError(f"Minimal length of name is 3")
        if len(v) > 100:
            raise ValueError(f"Maximal length of name 32")
        return v

    @pydantic.field_validator("password")
    @classmethod
    def secure_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError(f"Minimal length of password is 8")
        return v


class CreateUser(AbstractUser):
    name: str
    password: str
    email: str


class UpdateUser(AbstractUser):
    name: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None


SHEMA_CLASS = Type[CreateUser | UpdateUser]
SHEMA = CreateUser | UpdateUser
