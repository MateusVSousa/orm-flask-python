from flask import Flask, Blueprint
from app.routes.vaccine_routes import bp as bp_vaccine

bp_api = Blueprint('api',__name__)



def init_app(app:Flask):

    bp_api.register_blueprint(bp_vaccine)

    app.register_blueprint(bp_api)
