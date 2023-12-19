from flask import Flask
from .views import views
from .auth import auth


def create_app():
    app = Flask(__name__)
    
    app.secret_key = 'super secret key'

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app
