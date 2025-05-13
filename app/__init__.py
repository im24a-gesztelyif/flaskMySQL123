from flask import Flask
from app.routes import tasks, users, materials # import your routes


def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(tasks.app)
    app.register_blueprint(users.app)
    app.register_blueprint(materials.app)

    return app