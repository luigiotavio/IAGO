from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(Integer, primary_key=True)
    name = db.Column(String)
    email = db.Column(String, unique=True)
    occupation = db.Column(String)
    cell = db.Column(String)
    age = db.Column(Integer)
    gender = db.Column(String)
    subscription_id = db.Column(Integer, ForeignKey('subscription.id'))
    role = db.Column(String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'occupation': self.occupation,
            'cell': self.cell,
            'age': self.age,
            'gender': self.gender,
            'subscription_id': self.subscription_id,
            'role': self.role
        }
