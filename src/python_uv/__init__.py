from flask import Flask
from src.routes.user_routes import user_routes
from flask_cors import CORS

def create_app():
    app= Flask (__name__)
    #Resister blueprints
    app.register_blueprint(user_routes)
    
    CORS(app)

    @app.route("/")
    def hello():
        return {"message": "Hello, World!"}
    
    return app

