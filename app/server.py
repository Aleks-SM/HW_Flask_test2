import flask
from flask import views, jsonify, request
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

from app.models import Session, User
from app.error import HttpError
from app.shema import CreateUser, UpdateUser
from app.tools import validate

app = flask.Flask("app")
bcrypt = Bcrypt(app)


def hash_password(password: str):
    password = password.encode()
    return bcrypt.generate_password_hash(password).decode()


def check_password(password: str, hashed_password: str):
    password = password.encode()
    hashed_password = hashed_password.encode()
    return bcrypt.check_password_hash(password, hashed_password)


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(response: flask.Response):
    request.session.close()
    return response


@app.errorhandler(HttpError)
def error_handler(error):
    response = jsonify({"error": error.description})
    response.status_code = error.status_code
    return response


def get_user(user_id: int):
    user = request.session.get(User, user_id)
    if user is None:
        raise HttpError(404, "user not found")
        # return response
    return user


def add_user(user: User):
    try:
        request.session.add(user)
        request.session.commit()
    except IntegrityError as err:
        raise HttpError(409, "user already exists")


class UserView(views.MethodView):

    @property
    def session(self) -> Session:
        return request.session

    def get(self, user_id: int):
        user = get_user(user_id)
        return flask.jsonify(user.dict)

    def post(self, user_id: int):
        user_data = validate(CreateUser, request.json)
        user_data["password"] = hash_password(user_data["password"])
        user = User(**user_data)
        add_user(user)
        return jsonify({"id": user_id})

    def path(self, user_id: int):
        user = get_user(user_id)
        user_data = validate(UpdateUser, request.json)
        if "password" in user_data:
            user_data["password"] = hash_password(user_data["password"])
        for key, value in user_data.items():
            setattr(user, key, value)
            add_user(user)
        return jsonify({"id": user_id})

    def delete(self, user_id: int):
        user = get_user(user_id)
        self.session.delete(user)
        self.session.commit()
        return jsonify({"status": "ok"})


user_view = UserView.as_view("user_view")

app.add_url_rule("/users/<int: user_id>>", view_func=user_view, methods=["GET", "PATCH", "DELETE"])
app.add_url_rule("/users", view_func=user_view, methods=["POST"])

if __name__ == "__main__":
    app.run()
