'''Disclaimer: Envrionment variables are not being set properly.
zsh equivalent to bash.profile should be where environment variables live.
Security risk is noted.
'''
import os

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db' #os.eviron.get(SQLALCHEMY_DATABASE_URI)

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'austin.web.server@gmail.com' #os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = 'austinwebserver123' #os.environ.get('EMAIL_PASS')