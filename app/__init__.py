from flask import Flask
from app import db
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .auth import auth as auth_blueprint
from . import views,forms
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE


simple = SimpleMDE()
mail = Mail()
photos = UploadSet('photos',IMAGES)
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


# ...
def create_app(config_name):
    app = Flask(__name__)
    
      # configure UploadSet
    configure_uploads(app,photos)
    mail.init_app(app)
    simple.init_app(app)


    # ....

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # ...
