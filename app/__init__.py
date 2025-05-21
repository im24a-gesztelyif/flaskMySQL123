from flask import Flask
import os

def create_app():
    # Define the absolute path to your frontend folder
    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

    app = Flask(
        __name__,
        template_folder=os.path.join(frontend_path, 'templates'),
        static_folder=os.path.join(frontend_path, 'static')
    )

    # Register Blueprints
    from app.routes import main, tasks, users, materials, category, progress, priority, files, TaskMaterial
    app.register_blueprint(tasks.app)
    app.register_blueprint(users.app)
    app.register_blueprint(materials.app)
    app.register_blueprint(category.app)
    app.register_blueprint(progress.app)
    app.register_blueprint(priority.app)
    app.register_blueprint(files.app)
    app.register_blueprint(TaskMaterial.app)
    app.register_blueprint(main.app)

    return app
