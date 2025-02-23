DB_USERNAME = "root"
DB_PASSWORD = "123456789"
DB_NAME = "restaurant"
DB_HOST = "localhost" 

class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'SuperSecretKey'
    DEBUG = True
