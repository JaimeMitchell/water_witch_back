from app import db
from sqlalchemy import *
from sqlalchemy.dialects.postgresql import Geometry
from geoalchemy2 import *

class Fountain(db.Model):
    __tablename__ = "fountains"

    id = db.Column(db.Integer, primary_key=True)
    point = db.Column(Geometry('POINT'))
    name = db.Column(db.String, nullable=True)
    details = db.Column(db.String, nullable=True)
    borough = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'point': self.point,
            'name': self.name,
            'details': self.details,
            'borough': self.borough
        }

    @classmethod
    def to_object(cls, data_dict):
        return cls(
            point=data_dict["point"],
            name=data_dict["name"],
            details=data_dict["details"],
            borough=data_dict["borough"])
        
        from sqlalchemy.dialects.postgresql import ST_AsGeoJSON

# def point_to_geojson(point):
#     location_geojson = db.session.query(ST_AsGeoJSON(Point.location)).filter(Point.id==point.id).scalar()
#     return {
#       "type": "Feature",
#       "geometry": json.loads(location_geojson),
#       "properties": {
#         "name": point.name,
#         "details": point.details,
#         "borough": point.borough
#       }
#     }





# from app import db

# class Fountain(db.Model):
#     __tablename__ = "fountains"

#     id = db.Column(db.Integer, primary_key=True)
#     latitude= db.Column(db.Float(row[lat]), nullable=False)
#     longitude=db.Column(db.Float(row[lon]), nullable=False)
#     name = db.Column(db.String, nullable=True)
#     details = db.Column(db.String, nullable=True)
#     borough = db.Column(db.String, nullable=True)

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'latitude':self.latitude,
#             'longitude':self.longitude,
#             'name': self.name,
#             'details': self.details,
#             'borough': self.borough
#         }

#     @classmethod
#     def from_dict_to_object(cls, data_dict):
#         return cls(
#             latitude=data_dict["latitude"],
#             longitude=data_dict["longitude"],
#             name=data_dict["name"],
#             details=data_dict["details"],
#             borough=data_dict["borough"])
