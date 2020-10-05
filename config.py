DEBUG = True

USERNAME = 'myuser'
PASSWORD = 'mypassword'
SERVER = 'localhost'
DB = 'clients'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "my-secret-key"
