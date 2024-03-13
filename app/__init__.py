from flask import Flask
from .views.auth import auth_bp
from .views.dashboard import dashboard_bp
from .models.database import init_db
from flask_sqlalchemy import SQLAlchemy
from app.models import User

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações do aplicativo (opcional)
    
    # Inicializa o banco de dados
    init_db(app)

    # Registra os blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app
