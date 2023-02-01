from app import create_app, db
import csv
from app.models.fountain import Fountain


def getFountains():
    fountains = open("fountain.csv", "r")
    reader = csv.DictReader(fountains)

    list_of_fountains_to_add_to_db = []
    for fountain in reader:
        fountain_to_add = Fountain(
            latitude=float(fountain['latitude']),
            longitude=float(fountain['longitude']),
            name=fountain['name'],
            details=fountain['details'],
            borough=fountain['borough'],
            type='public_drinking_fountain',
            # phone=fountain['phone'],
            # email=fountain['email']
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

# IF I NEED TO GO BACK TO GEOJSON FORMAT, HERE'S EXAMPLE OF HOW I MIGHT GRAB NESTED VALUE
# def getFountains():
#     list_of_fountains_to_add_to_db = []
#     for fountain in fountains:
#         fountain_to_add = Fountain(
#             latitude=fountain.features[0].property.latitude,
#             longitude=fountain.features[0].property.longitude,
# ...
