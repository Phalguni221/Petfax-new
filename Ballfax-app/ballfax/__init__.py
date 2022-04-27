from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate
from flask import (Blueprint, render_template, redirect, request)



bp = Blueprint('reptile', __name__, url_prefix="/reptiles")         

# print(pets)

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Phalguni2025@localhost:5432/ballpy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False      


#migrations 
    from . import ballmodels 
    ballmodels.db.init_app(app) 
    migrate = Migrate(app, ballmodels.db)
    
    # index route
    @app.route('/reptiles')
    def ballindex(): 
            return 'Hello, Reptiles!'