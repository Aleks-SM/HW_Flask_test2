from pydantic import ValidationError
from flask_scrypt import generate_password_hash, generate_random_salt, check_password_hash
from error import HttpError

def validate(schema_cls, json_data: dict | list):
    try:
        return schema_cls(**json_data).dict(exclude_unset=True)
    except ValidationError as er:
        error = er.errors()[0]
        error.pop("ctx", None)
        error.pop("url", None)
        raise HttpError(400, error)

def hash_password(user_password):
    salt = generate_random_salt().decode()
    password = generate_password_hash(user_password, salt).decode()
    return {'salt': salt, 'password': password}

def check_password(password, hash, salt):
    return check_password_hash(password.encode(), hash.encode(), salt.encode())