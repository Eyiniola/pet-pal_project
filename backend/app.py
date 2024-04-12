#!/usr/bin/python3

from flask import Flask
# from flask_cors import CORS
from controllers.accesoryController import accesory
from controllers.medicalController import medical
from controllers.adoptController import adopt
from services.database import db
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

#  configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://petPalAdmin:petPalAdmin1244@localhost/pet_pal_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db.init_app(app)

#  register the blueprints
app.register_blueprint(accesory)
app.register_blueprint(medical)
app.register_blueprint(adopt)

# CORS(app)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
