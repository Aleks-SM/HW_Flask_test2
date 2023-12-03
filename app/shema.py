import pydantic
from typing import Optional

class AbstractUser(pydantic.BaseModel):
    @pydantic.field_validator("name")
    @classmethod
    def name_length(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError(f"Minimal length of name is 3")
        if len(v) > 100:
            raise ValueError(f"Maximal length of name 32")
        return v

    @pydantic.field_validator("passord")
    @classmethod
    def secure_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError(f"Minimal length of passord is 8")
        return v


class CreateUser(AbstractUser):
    name: str
    password: str


class UpdateUser(AbstractUser):
    name: Optional[str]
    password: Optional[str]