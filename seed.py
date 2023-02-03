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
            type=fountain['type']
        )
        if fountain_to_add.type == '':
            fountain_to_add.type = 'public drinking fountains'
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

