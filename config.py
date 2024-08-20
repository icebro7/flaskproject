class Config:
    def __init__(self):
        self.DATABASE_PATH = "database/empdata.db"


class userConfig:
    DEBUG = True
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'userdata'
    USERNAME = 'root'
    PASSWORD = '7777777'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    # secret_key
    SECRET_KEY = 'kdjklfjkd87384hjdhjh'


class DevelopmentConfig(userConfig):
    ENV = 'development'


class ProductionConfig(userConfig):
    ENV = 'production'
    DDEBUG = False


employ = Config()
