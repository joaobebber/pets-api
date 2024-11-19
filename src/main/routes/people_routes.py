from flask import Blueprint, jsonify, request

from src.views.http_types.http_request import HttpRequest
from src.main.composer.person_creator_composer import person_creator_composer
from src.main.composer.person_finder_composer import person_finder_composer


people_routes_bp = Blueprint(name="people_routes", import_name=__name__)

@people_routes_bp.route(rule="/person", methods=["POST"])
def create_person():
    http_request = HttpRequest(body=request.json)

    view = person_creator_composer()
    http_response = view.handle(http_request=http_request)

    return jsonify(http_response.body), http_response.status_code

@people_routes_bp.route(rule="/people/<person_id>", methods=["GET"])
def find_person(person_id: str):
    http_request = HttpRequest(param={ "person_id": person_id })

    view = person_finder_composer()
    http_response = view.handle(http_request=http_request)

    return jsonify(http_response.body), http_response.status_code
