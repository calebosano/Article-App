# Flask configuration settings
FLASK_DEBUG = True  # Do not use debug mode in production
SECRET_KEY = 'Thisismysecretkey'

# Database settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = True

