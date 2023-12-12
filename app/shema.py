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
        if 50 < len(v) < 3:
            raise ValueError(f"Name length must be from 3 to 50 characters")
        return v

    @pydantic.field_validator("password")
    @classmethod
    def secure_password(cls, v: str) -> str:
        if 50 < len(v) < 8:
            raise ValueError(f"Password length must be from 8 to 50 characters")
        return v


class CreateUser(AbstractUser):
    name: str
    password: str
    email: str


class UpdateUser(AbstractUser):
    name: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None

class LoginUser(AbstractUser):
    email: str
    password: str
