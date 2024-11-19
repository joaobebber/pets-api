from flask import Flask
from flask_cors import CORS

from src.main.routes.pets_routes import pets_routes_bp
from src.main.routes.people_routes import people_routes_bp
from src.models.sqlite.settings.connection import db_connection_handler


db_connection_handler.connect_to_db()

app = Flask(import_name=__name__)

CORS(app=app)

app.register_blueprint(blueprint=pets_routes_bp)
app.register_blueprint(blueprint=people_routes_bp)
