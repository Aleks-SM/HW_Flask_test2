from pydantic import ValidationError
from app.shema import SHEMA_CLASS
from app.error import HttpError

def validate(schema_cls: SHEMA_CLASS, json_data: dict | list):
    try:
        return schema_cls(**json_data).dict(exclude_unset=True)
    except ValidationError as er:
        error = er.errors()[0]
        error.pop("ctx", None)
        raise HttpError(400, error)
