from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    
    #Creates app configuration
    app.config.from_object(config_options[config_name])
    
    #Initializing flask extensions
    bootstrap.init_app(app)
    
    #Register blueprint
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .request import configure_request
    configure_request(app)
    
    return app