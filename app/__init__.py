from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

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
