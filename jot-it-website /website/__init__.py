#__init__.py
#Creates web app, creates database
#Treats website folder as a package
#Developer: Shavon Thadani
#23/08/'21
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = "database.db"
def create_app():
    #Create web app and database
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aklsdfjal faskjdnfaskjdfn'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    #import blueprints
    from .views import views
    from .auth import auth
    #register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    # import database models
    from .models import User, Note
    create_database(app)
    #start off on login page
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def login_manager(id):
        return User.query.get(int(id))


    return app
#create database
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Created database")
