import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'secretkey')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False