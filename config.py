import os


class  Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://ebay:qwerty@localhost/sendit'
  
class  ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')

class DevConfig(Config):
  
    DEBUG = True
  
class TestConfig(Config):
  pass

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}    