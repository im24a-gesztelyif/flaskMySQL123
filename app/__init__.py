from flask import Flask, session
from flask_wtf import CSRFProtect
import os

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__, 
                template_folder='templates', 
                static_folder='static')
    
    @app.context_processor
    def inject_user():
        return dict(username=session.get('username'))

    app.secret_key = os.urandom(24)
    csrf.init_app(app)

    # Register Blueprints
    from app.routes import (main, tasks, users, materials, category, 
                            progress, priority, files, TaskMaterial, 
                            login)
    
    app.register_blueprint(tasks.app)
    app.register_blueprint(users.app)
    app.register_blueprint(materials.app)
    app.register_blueprint(category.app)
    app.register_blueprint(progress.app)
    app.register_blueprint(priority.app)
    app.register_blueprint(files.app)
    app.register_blueprint(TaskMaterial.app)
    app.register_blueprint(main.app)
    app.register_blueprint(login.app)

    return app
