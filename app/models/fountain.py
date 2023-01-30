from app import db
from sqlalchemy import *
from geoalchemy2.functions import ST_AsGeoJSON, ST_Intersects
from geoalchemy2.types import Geometry
# from sqlalchemy.dialects.postgresql import ST_AsGeoJSON, ST_Intersects

# class Fountain(db.Model):
#     __tablename__ = "fountains"

#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     geometry = db.Column(Geometry('POINT'))
#     name = db.Column(db.String, nullable=True)
#     details = db.Column(db.String, nullable=True)
#     borough = db.Column(db.String, nullable=True)

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'geometry': self.geometry,
#             'name': self.name,
#             'details': self.details,
#             'borough': self.borough
#         }

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'geometry': self.geometry.wkt,
    #         'name': self.name,
    #         'details': self.details,
    #         'borough': self.borough,

    #     }

    # ?

    # @classmethod
    # def get_clustered_markers(cls, bbox):
    #     """
    #     Get the markers within the bounding box, optimized for clustering.
    #     :param bbox: list of coordinates representing the bounding box
    #     :return: list of Fountain objects
    #     """
    #     polygon = func.ST_GeomFromText(
    #         f'POLYGON(({bbox[0]} {bbox[1]}, {bbox[2]} {bbox[1]}, {bbox[2]} {bbox[3]}, {bbox[0]} {bbox[3]}, {bbox[0]} {bbox[1]}))')
    #     return cls.query.filter(ST_Intersects(cls.geometry, polygon)).all()

    # def point_to_geojson(point):
    #     fountain_geojson = db.session.query(ST_AsGeoJSON(Fountain.geometry)).filter(Fountain.id == point.id).scalar()
    #     return {
    #         "type": "Feature",
    #         "geometry": json.loads(fountain_geojson),
    #         "properties": {
    #             "name": point.name,
    #             "details": point.details,
    #             "borough": point.borough
    #         }
    #     }

from app import db

class Fountain(db.Model):
    __tablename__ = "fountains"

    id = db.Column(db.Integer, primary_key=True)
    latitude= db.Column(db.Float, nullable=False)
    longitude=db.Column(db.Float, nullable=False)
    name = db.Column(db.String, nullable=True)
    details = db.Column(db.String, nullable=True)
    borough = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'latitude':self.latitude,
            'longitude':self.longitude,
            'name': self.name,
            'details': self.details,
            'borough': self.borough
        }

    @classmethod
    def to_object(cls, data_dict):
        return cls(
            latitude=data_dict["latitude"],
            longitude=data_dict["longitude"],
            name=data_dict["name"],
            details=data_dict["details"],
            borough=data_dict["borough"])
