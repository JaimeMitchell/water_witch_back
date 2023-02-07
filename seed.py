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
            address=fountain['address'],
            name=fountain['name'],
            details=fountain['details'],
            borough=fountain['borough'],
            type=fountain['type']

        )
        if fountain_to_add.type == '':
            fountain_to_add.type = 'Park Drinking Fountain'
        list_of_fountains_to_add_to_db.append(fountain_to_add)
        if fountain_to_add.borough == 'M':
            fountain_to_add.borough = 'Manhattan'
        if fountain_to_add.borough == 'B':
            fountain_to_add.borough = 'Brooklyn'
        if fountain_to_add.borough == 'X':
            fountain_to_add.borough = 'Bronx'
        if fountain_to_add.borough == 'Q':
            fountain_to_add.borough = 'Queens'
        if fountain_to_add.borough == 'R':
            fountain_to_add.borough = 'Staten Island'
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
