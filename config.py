from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'SuperSecretKey'
    DEBUG = True

    def __str__(self):
        return f"SQLALCHEMY_DATABASE_URI: {self.SQLALCHEMY_DATABASE_URI}"