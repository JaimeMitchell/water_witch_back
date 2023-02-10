from app import db
from sqlalchemy import *


class Fountain(db.Model):
    __tablename__ = "fountains"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    address = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=False)
    details = db.Column(db.String, nullable=False)
    borough = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'address': self.address,
            'name': self.name,
            'details': self.details,
            'borough': self.borough,
            'type': self.type,
            'phone': self.phone,
            'email': self.email,
        }

    @classmethod
    def to_object(cls, data_dict):
        return cls(
            latitude=data_dict["latitude"],
            longitude=data_dict["longitude"],
            address=data_dict["address"],
            name=data_dict["name"],
            details=data_dict["details"],
            borough=data_dict["borough"],
            type=data_dict["type"],
            phone=data_dict["phone"],
            email=data_dict["email"]
        )
