import flask

from models import Session, User
from error import HttpError

from tools import validate


app = flask.Flask("app")


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


user_view = UserView.as_view("user_view")

app.add_url_rule("/users/<int:user_id>", view_func=user_view, methods=["GET", "PATCH", "DELETE"])
app.add_url_rule("/users", view_func=user_view, methods=["POST"])
app.add_url_rule("/login", view_func=login_view, methods=["POST"])

if __name__ == "__main__":
    app.run()
