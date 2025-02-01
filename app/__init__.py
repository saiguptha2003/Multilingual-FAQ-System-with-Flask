from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_redis import FlaskRedis
from flask_migrate import Migrate
from dotenv import load_dotenv
from .models import db
import os
redis = FlaskRedis()

migrate = Migrate()

def create_app(config_class='app.config.Config'):
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    redis.init_app(app)
    migrate.init_app(app, db)

    CORS(app)  
    from app import views
    app.register_blueprint(views.bp)

    return app
