from flask import Flask
from app.routes import tasks, users, materials  # import your routes


def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(tasks.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(materials.bp)

    return app