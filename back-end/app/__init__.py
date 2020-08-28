from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

# Flask-SQLAlchemy plugin
db = SQLAlchemy()

# Flask-Migrate plugin
migrate = Migrate()

# _ini_.py的两个作用为：一是包含应用工厂，二是告诉python将文件夹应当视为一个包


def create_app(config_class=Config):
    # 初始化项目
    app = Flask(__name__)
    app.config.from_object(config_class)
    # enable CORS
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)
    # 注册blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


from app import models

