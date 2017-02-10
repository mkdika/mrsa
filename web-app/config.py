class Config(object):
    DEBUG = False
    TESTING = False

class Development(Config):
    SECRET_KEY = 'lw8HfA7q4nOhvCU50nXZZIcia0YAWHnLGb1gqDoBTJedNQZe2YEH1QCBaxYBYhSeWp70lsK41ux0syDVynAcWm2RIhXPXXqDC4RKC9GXR9TpQgSKPRFw1mjxTcGiqBSJ'
    #DATABASE   = 'sentiment.db'
    DB_TYPE    = 'mysql'     # or sqlite
    DATABASE   = 'sentiment'
    DB_HOST    = 'localhost'
    DB_USER    = 'sentiment'
    DB_PASSWORD= 'sentiment'
