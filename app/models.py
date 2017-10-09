from app import app
from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(128), index = True, unique = True)
    cost = db.Column(db.Integer, index = True, unique = False)
    jpeg = db.Column(db.String(128), index = True, unique = True)
    properties = db.Column(db.Text, index = True, unique = False)

    def __repr__(self):
        return '<Product {}>'.format(self.name)

with app.app_context():
    db.create_all()
