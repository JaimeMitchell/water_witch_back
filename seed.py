from app import create_app, db
import csv
from app.models.fountain import Fountain


def getFountains():
    fountains = open("fountain.csv", "r")
    reader= csv.DictReader(fountains)

    list_of_fountains_to_add_to_db = []
    for fountain in reader:
        fountain_to_add = Fountain(
            latitude=float(fountain['latitude']),
            longitude=float(fountain['longitude']),
            name=fountain['name'],
            details=fountain['details'],
            borough=fountain['borough']
        )
        list_of_fountains_to_add_to_db.append(fountain_to_add)
    return list_of_fountains_to_add_to_db


def load():
    app = create_app()

    fountains = getFountains()

    with app.app_context():
        db.session.add_all(fountains)
        db.session.commit()


def main():
    load()


if __name__ == "__main__":
    main()


# from app import db
# from app import create_app, db
# from app.models.fountain import Fountain

# fountains = [
#     {
#         "latitude": 40.666701390972364,
#         "longitude": -73.862594500714295,
#         "name": "Pink Playground",
#         "details": "In Playground",
#         "borough": "B"
#     },
#     {
#         "latitude": 40.6756201057255,
#         "longitude": -73.863013059621238,
#         "name": "Belmont Playground",
#         "details": "In Playground",
#         "borough": "B"
#     },

#     {
#         "latitude": 40.674530476243746,
#         "longitude": -73.864882054307543,
#         "name": "Robert E. Venable Park",
#         "details": "Just Outside Playground",
#         "borough": "B"

#     }

# ]

# fountains = [
#     {
#         "type": "FeatureCollection",
#         "features": [
#             {"type": "Feature",
#             "properties": { "name": "Pink Playground",
#             "details": "In Playground",
#             "borough": "B",
#             "latitude": 40.666701390972364,
#             "longitude": -73.862594500714295 }
#             }
#         ]
#     }
# ]

# THIS IS JUST A REFERENCE TO LOOK AT, IT LIVES IN UR MODEL
# class Fountain(db.Model):
#     __tablename__ = "fountains"

#     id = db.Column(db.Integer, primary_key=True)
#     latitude= db.Column(db.Float, nullable=False)
#     longitude=db.Column(db.Float, nullable=False)
#     name = db.Column(db.String, nullable=False)
#     details = db.Column(db.String, nullable=False)
#     borough = db.Column(db.String, nullable=False)


# def getFountains():
#     list_of_fountains_to_add_to_db = []
#     for fountain in fountains:
#         fountain_to_add = Fountain(
#             latitude=fountain.features[0].property.latitude,
#             longitude=fountain.features[0].property.longitude,
#             name="Name",
#             details="Details",
#             borough="Borough"
#         )
#         list_of_fountains_to_add_to_db.append(fountain_to_add)
#     return list_of_fountains_to_add_to_db
