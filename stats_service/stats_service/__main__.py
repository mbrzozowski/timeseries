from flask import Flask


from stats_service import config
from stats_service.api.version_one import get_version_one_api
from stats_service.db import db


def get_flask_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    app.register_blueprint(get_version_one_api())
    return app


def main():
    app = get_flask_app()
    app.run(host=config.APP_INTERFACE,
            port=config.APP_PORT,
            debug=config.APP_DEBUG)


if __name__ == "__main__":
    main()
