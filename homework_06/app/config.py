import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://dbuser:dbuserpass@localhost:5432/homework06",
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "8dfcdde8-6a35-4dff-a65a-209a066dec7b",
)

BOOTSTRAP_SERVE_LOCAL = True
BOOTSTRAP_BTN_SIZE = 'md'

class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"
    PORT = 5000
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    BOOTSTRAP_SERVE_LOCAL = BOOTSTRAP_SERVE_LOCAL
    BOOTSTRAP_BTN_SIZE = BOOTSTRAP_BTN_SIZE

class ProductionConfig(Config):
    ENV = "production"
    PORT = 80

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True