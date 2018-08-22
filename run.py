from app import settings
from app.api.v1.stackendpoints import api
from app.api.v1.stackendpoints.answers import ns as users_namespace
from app.api.v1.stackendpoints.questions import ns as questions_namespace
from config import create_app

config_name = settings.APP_ENVIRONMENT_SETTINGS  # config_name = "development"
app = create_app(config_name)

api.init_app(app)
api.add_namespace(questions_namespace)
api.add_namespace(users_namespace)

if __name__ == '__main__':
    app.run()
