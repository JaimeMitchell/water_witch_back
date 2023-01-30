from app import db
from app.models.fountain import Fountain
from flask import Blueprint, jsonify, abort, make_response, request
from dotenv import load_dotenv
from sqlalchemy.sql.expression import select, func
# import requests, if i want to incorporate an 3rd party api and/or bot (see slack bot in tasklist-api repo)
# import os, if i want to incorporate an 3rd party api and/or bot (see slack bot in tasklist-api repo)
import os
import requests
from geoalchemy2 import Geometry, WKTElement
from geopandas import GeoDataFrame

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


# Route for handling the form submission
# @fountain_bp.route('/add_fountain', methods=['POST'])
# def add_fountain():
#     # Get the data from the form
#     data = request.get_json()

#     # Convert the data to a GeoDataFrame
#     df = GeoDataFrame(data, geometry=[Point(x, y) for x, y in zip(data['longitude'], data['latitude'])])
#     df['geometry'] = df['geometry'].apply(lambda x: WKTElement(x.wkt, srid=4326))

#     # Add the new fountain to the table
#     df.to_sql('fountains', engine, if_exists='append', index=False, dtype={'geometry': Geometry('POINT', srid= 4326)})

#     # Re-create the spatial index on the geometry column
#     db.session.execute("CREATE INDEX name_of_index ON fountains USING GIST (geometry);")
#     db.session.commit()

#     return jsonify({'message': 'Success'})

# STANDARD GET ALL FUNCTION

@fountain_bp.route("", strict_slashes=False, methods=["GET"])
def read_all_fountains():
    fountains = Fountain.query.all()
    fountain_response = [fountain.to_dict() for fountain in fountains]

    return make_response(jsonify(fountain_response), 200)

# #VERSION 2 GET ALL 

# @fountain_bp.route("", strict_slashes=False, methods=["GET"])
# def read_all_fountains():
#     fountains= Fountain.query.all()
#     response = {"type": "FeatureCollection","features": []}
    
#     for fountain in fountains:
#         feature={"type": "Feature", "properties": {"name": fountain.name, "details": fountain.details,"borough":fountain.borough }, "geometry": {"type": "Point", "coordinates": [fountain.latitude, fountain.longitude]}}
#         response['features'].append(feature)

#     return make_response(jsonify(response), 200)

#VERSION 3 GET ALL 

@fountain_bp.route("", strict_slashes=False, methods=["GET"])
def read_all_fountains():
    fountains= Fountain.query.all()
    response = {"type": "FeatureCollection","features": []}
    geometry= response["geometry"]["coordinates"] #value of this is [lat,lon]
    print(geometry)
    for fountain in fountains:
        feature={"type": "Feature", "properties": {"name": fountain.name, "details": fountain.details,"borough":fountain.borough }, "geometry":{"type": "Point", "coordinates": [fountain.latitude, fountain.longitude]}}
        response['features'].append(feature)

    return make_response(jsonify(response), 200)



# STANDARD POST FUNCTION
@ fountain_bp.route("", strict_slashes=False, methods=["POST"])
def add_fountain():
    request_body= request.get_json()
    new_fountain= Fountain.to_object(request_body)
    db.session.add(new_fountain)
    db.session.commit()
    return make_response(jsonify({"fountain": new_fountain.to_dict()}), 201)

# STANDARD DELETE FUNCTION
@ fountain_bp.route("/<id>", strict_slashes=False, methods=["DELETE"])
def delete_fountain(id):
    fountain= validate_model(Fountain, id)
    db.session.delete(fountain)
    db.session.commit()
    return make_response(jsonify({"details": f"fountain {id} '{fountain.name}' successfully deleted"}), 200)
