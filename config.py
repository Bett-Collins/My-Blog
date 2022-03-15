import os
import re



class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:2020@localhost/myblogs'
    QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'



class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://")
        
    # uri = os.getenv("DATABASE_URL")  # or other relevant config var
    
    # if uri.startswith("postgres://"):
        
    #    uri = uri.replace("postgres://", "postgresql://", 1)
        
        
   

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:2020@localhost/myblogs'


    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}