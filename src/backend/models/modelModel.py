from database.database import db
from sqlalchemy import Column, Integer, String

class Model(db.Model):
    __tablename__ = 'model'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String, unique=True)
    max_token = db.Column(Integer)
    min_token = db.Column(Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'max_token': self.max_token,
            'min_token': self.min_token
        }