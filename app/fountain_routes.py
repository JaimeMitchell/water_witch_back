from app import db
from flask import Blueprint, jsonify, abort, make_response, request
from dotenv import load_dotenv
from sqlalchemy.sql.expression import func
from app.models.fountain import Fountain
# import requests, if i want to incorporate an 3rd party api and/or bot (see slack bot in tasklist-api repo)
# import os, if i want to incorporate an 3rd party api and/or bot (see slack bot in tasklist-api repo)

load_dotenv()
# INSTANIATE BLUEPRINT FOR ROUTES
# Create a blueprint for the fountain routes
fountain_bp = Blueprint('fountain_bp', __name__, url_prefix='/fountains')

# A helper function to validate the fountain model


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        # If the model id is not a valid integer, return a 400 error
        abort(make_response({"details": "Invalid Data"}, 400))
    model = cls.query.get(model_id)

    if not model:
        # If the model with the given id is not found, return a 404 error
        abort(make_response(
            {"details": f"{cls.__name__} {model_id} not found"}, 404))
    return model


@fountain_bp.route("", strict_slashes=False, methods=["GET"])
def read_all_fountains():
    fountains = Fountain.query.all()
    fountain_response = [fountain.to_dict() for fountain in fountains]

    return make_response(jsonify(fountain_response), 200)


@fountain_bp.route("", strict_slashes=False, methods=["POST"])
def add_fountain():
    request_body = request.get_json()
    new_fountain = Fountain.from_dict_to_object(request_body)
    db.session.add(new_fountain)
    db.session.commit()
    return make_response(jsonify({"fountain": new_fountain.to_dict()}), 201)


@fountain_bp.route("/<id>", strict_slashes=False, methods=["DELETE"])
def delete_fountain(id):
    fountain = validate_model(Fountain, id)
    db.session.delete(fountain)
    db.session.commit()
    return make_response(jsonify({"details": f"fountain {id} '{fountain.name}' successfully deleted"}), 200)
