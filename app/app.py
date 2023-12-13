from flask.ext.sqlAlchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user


db = SQLALchemy(app)

# Инициализируем и задаем действие "входа"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Задаем обработчик, возвращающий пользователя по Id, либо None. Здесь пользователь запрашивается из базы.
@login_manager.user_loader
def load_user(userid):
    from models import User
    return User.query.get(int(userid))

# Задаем обработчик before_request, в котором добавляем к глобально-локальному контексту текущего пользователя  
@app.before_request
def before_request():
    g.user = current_user
