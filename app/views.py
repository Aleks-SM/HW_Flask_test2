from flask import views, jsonify, request
from sqlalchemy.exc import IntegrityError

from models import User, Session
from error import HttpError
from shema import CreateUser, UpdateUser, LoginUser
from tools import validate, hash_password, check_password


def get_user(user_id: int):
    user = request.session.get(User, user_id)
    if user is None:
        raise HttpError(404, "user not found")
    return user


def add_user(user: User):
    try:
        request.session.add(user)
        request.session.commit()
    except IntegrityError:
        raise HttpError(409, "user already exists")

class AbstractView(views.MethodView):
    @property
    def session(self) -> Session:
        return request.session


class UserView(AbstractView):
    def get(self, user_id: int):
        user = get_user(user_id)
        return jsonify(user.dict)

    def post(self):
        user_data = validate(CreateUser, request.json)
        user_data["password"] = hash_password(user_data["password"])
        user = User(**user_data)
        add_user(user)
        return jsonify({"id": user.user_id})

    def patch(self, user_id: int):
        user = get_user(user_id)
        user_data = validate(UpdateUser, request.json)
        if "password" in user_data:
            user_data["password"] = hash_password(user_data["password"])
        for key, value in user_data.items():
            setattr(user, key, value)
            add_user(user)
        return jsonify({"id": user.user_id})

    def delete(self, user_id: int):
        user = get_user(user_id)
        self.session.delete(user)
        self.session.commit()
        return jsonify({"status": "ok"})


class LoginView(AbstractView):
    def post(self):
        user_data = validate(LoginUser, request.json)
        user_data["password"] = hash_password(user_data["password"])
        user = User(**user_data)
        add_user(user)
        return jsonify({"id": user.user_id})