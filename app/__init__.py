from flask_sqlalchemy import SQLAlchemy
from . import bootstrap
from flask_login import LoginManager
from .auth import auth as auth_blueprint
from . import views,forms


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


# ...
def create_app(config_name):
    app = Flask(__name__)

    # ....

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # ...
