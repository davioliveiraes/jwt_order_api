from flask import Flask
from src.main.routes.auth_routes import auth_routes
from src.main.routes.order_routes import order_routes

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_routes)
    app.register_blueprint(order_routes)

    return app
