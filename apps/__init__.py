from flask import Flask
from apps.user.view import user_bp
from exts import db
from config import DevelopmentConfig

def create_app():
    app = Flask(__name__,template_folder='../templates', static_folder='../static')
    app.config.from_object(DevelopmentConfig)

    db.init_app(app=app)

    app.register_blueprint(user_bp)

    return app