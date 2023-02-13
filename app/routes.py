from app import db
from app.models.fountain import Fountain
from flask import Blueprint, jsonify, abort, make_response, request
from dotenv import load_dotenv
from sqlalchemy.sql.expression import select, func
# import requests, if i want to incorporate an 3rd party api and/or bot (see slack bot in fountainlist-api repo)
# import os, if i want to incorporate an 3rd party api and/or bot (see slack bot in fountainlist-api repo)
import os


load_dotenv()

# INSTANIATE BLUEPRINT FOR ROUTES
# Create a blueprint for the fountain routes
fountain_bp = Blueprint('fountain', __name__, url_prefix='/fountains')

# A helper function to validate the fountain model
# In summary, this function checks if the provided model_id is a valid integer and if it exists in the database table represented by the cls model. If it exists, it returns the model, otherwise it returns a error message.


def validate_model(cls, model_id):
    # Then the function uses the cls argument, which is expected to be a SQLAlchemy model class, to query the database for a record with the same id as the model_id argument. If no such record is found, the function returns a HTTP status code of 404 (Not Found) and a JSON object containing an error message.
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
    # If the record is found, the function returns the model, which is a SQLAlchemy object representing the record.
    return model


# BASIC NO FRILLS GET ALL

# @fountain_bp.route("", strict_slashes=False, methods=["GET"])
# def read_all_fountains():
#     fountains = Fountain.query.all()
#     fountain_response = [fountain.to_dict() for fountain in fountains]

#     return make_response(jsonify(fountain_response), 200)

# FILTER BY Type, Borough, Address (ex:  Type: Private Hose Bibb  Borough: Manhattan  Address 200 11th st, New York, NY, 10003)

@fountain_bp.route("", strict_slashes=False, methods=["GET"])
def get_all_fountain():
    type_query = request.args.get("type")
    borough_query = request.args.get("borough")
    address_query = request.args.get("address")
    fountain_query = Fountain.query
    if type_query:
        fountain_query = fountain_query.filter_by(type=type_query)

    if borough_query:
        fountain_query = fountain_query.filter_by(borough=borough_query)

    if address_query:
        fountain_query = fountain_query.filter_by(address=address_query)
    # fountains = fountain_query.all()
    # SORT
    fountains = fountain_query.order_by(Fountain.id).all()
    fountain_response = [fountain.to_dict() for fountain in fountains]

    return jsonify(fountain_response)


@fountain_bp.route("/<id>", strict_slashes=False, methods=["GET"])
def read_one_fountain(id):
    fountain = validate_model(Fountain, id)
    return {"fountain": fountain.to_dict()}, 200


# POST (FORM TO ADD WATER ENTITY)

@ fountain_bp.route("", strict_slashes=False, methods=["POST"])
def add_fountain():
    request_body = request.get_json()
    try:
        new_fountain = Fountain.to_object(request_body)
    except KeyError:
        abort(make_response({
            "details": "Invalid data"
        }, 400))
    db.session.add(new_fountain)
    db.session.commit()
    return make_response(jsonify((new_fountain.to_dict())), 201)


# UPDATE ONE

@fountain_bp.route("/<int:id>", strict_slashes=False, methods=["PUT"])
def update_fountain(id):
    request_body = request.get_json()
    fountain = validate_model(Fountain, id)

    if "latitude" in request_body:
        fountain.latitude = request_body["latitude"]

    if "longitude" in request_body:
        fountain.longitude = request_body["longitude"]

    if "address" in request_body:
        fountain.address = request_body["address"]

    if "name" in request_body:
        fountain.name = request_body["name"]

    if "details" in request_body:
        fountain.details = request_body["details"]

    if "borough" in request_body:
        fountain.borough = request_body["borough"]

    if "type" in request_body:
        fountain.borough = request_body["type"]

    if "phone" in request_body:
        fountain.borough = request_body["phhone"]

    if "email" in request_body:
        fountain.borough = request_body["email"]

    db.session.commit()

    return make_response(jsonify({"fountain": fountain.to_dict()}), 200)


# DELETE ONE

@ fountain_bp.route("/<id>", strict_slashes=False, methods=["DELETE"])
def delete_fountain(id):
    fountain = validate_model(Fountain, id)
    db.session.delete(fountain)
    db.session.commit()
    return make_response(jsonify({"details": f"fountain {id} '{fountain.name}' successfully deleted"}), 200)


# DELETE ALL WATER SOURCES (ONLY FOR DEV, GET RID OF THIS IN DEPLOYMENT)

