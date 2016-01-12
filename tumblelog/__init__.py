from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log",
                                  'HOST': "192.168.1.33",
                                  'PORT': 27017}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

# client = pymongo.MongoClient(host='192.168.1.33', port=27017)
# if 'MONGODB_SETTINGS' in config:
#     # Connection settings provided as a dictionary.
#     connection = _create_connection(config['MONGODB_SETTINGS'])
# else:
#     # Connection settings provided in standard format.
#     settings = {'alias': config.get('MONGODB_ALIAS', None),
#                 'db': config.get('MONGODB_DB', None),
#                 'host': config.get('MONGODB_HOST', None),
#                 'password': config.get('MONGODB_PASSWORD', None),
#                 'port': config.get('MONGODB_PORT', None),
#                 'username': config.get('MONGODB_USERNAME', None)}

# db = MongoEngine(app)
db = MongoEngine(app, app.config)


def register_blueprints(app):
    # prevents circular imports
    from tumblelog.views import posts
    from tumblelog.admin import admin

    app.register_blueprint(posts)
    app.register_blueprint(admin)


register_blueprints(app)


if __name__ == '__main__':
    app.run()



