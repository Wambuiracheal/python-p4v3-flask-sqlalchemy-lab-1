from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from flask import jsonify

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(49), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Earthquake id={self.id} magnitude={self.magnitude} location={self.location} year={self.year}>'

    def serialize(self):
        return {
            'id': self.id,
            'magnitude': self.magnitude,
            'location': self.location,
            'year': self.year,
            'year': self.year
        }


