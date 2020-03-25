from flask import Flask, g

#takes blueprints (currently just from routes.py, can be expanded to multiple blueprints) and builds WSGI app object based on routes

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from src import routes

        app.register_blueprint(routes.bp)

        return app
