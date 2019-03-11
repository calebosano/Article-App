
from flask import Flask
from database.db_models import db
from config import FLASK_DEBUG, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from appfrontend.views import articles
from backend.views import users


# Creating and starting the flask app
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    app.register_blueprint(articles)
    app.register_blueprint(users)

    db.init_app(app)
    return app


if __name__ == '__main__':
    create_app().run(debug=FLASK_DEBUG)
