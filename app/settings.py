# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

APP_ENVIRONMENT_SETTINGS = "production"
SECRET = "my-second-Challenge-deploying-api-endpoints"


def FLASK_DEBUG():
    return True


def FLASK_SERVER_NAME():
    return None


def SQLALCHEMY_DATABASE_URI():
    return None


def SQLALCHEMY_TRACK_MODIFICATIONS():
    return None
