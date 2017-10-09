from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:qwerty@localhost/flask_db'
db = SQLAlchemy(app)

from app import views, models
app.secret_key = 'some secret key'

admin = Admin(app, name='YMarket', template_mode='bootstrap3')

# Flask and Flask-SQLAlchemy initialization here
admin.add_view(ModelView(models.Product, db.session))
