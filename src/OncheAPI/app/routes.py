from src.OncheAPI.app.controllers.database_controller import database_controller
from src.OncheAPI.app.controllers.user_controller import user_controller
from src.OncheAPI.app.controllers.link_controller import link_controller

def init_app(app):
    app.register_blueprint(user_controller, url_prefix='/user')
    app.register_blueprint(database_controller, url_prefix='/data')
    app.register_blueprint(link_controller, url_prefix='/')
