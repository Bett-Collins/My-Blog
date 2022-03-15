import os



class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = '123456'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:2020@localhost/blogs'
    QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'arapbett@gmail.com'
    MAIL_PASSWORD = '2020'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        
    #     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://")
   

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:2020@localhost/blogs'


    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}