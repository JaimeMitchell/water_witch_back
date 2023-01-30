from app import db
from sqlalchemy import *
from geoalchemy2.functions import ST_AsGeoJSON, ST_Intersects
from geoalchemy2.types import Geometry


from app import db

class Fountain(db.Model):
    __tablename__ = "fountains"

    id = db.Column(db.Integer, primary_key=True)
    latitude= db.Column(db.Float, nullable=False)
    longitude=db.Column(db.Float, nullable=False)
    name = db.Column(db.String, nullable=False)
    details = db.Column(db.String, nullable=False)
    borough = db.Column(db.String, nullable=False)

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
