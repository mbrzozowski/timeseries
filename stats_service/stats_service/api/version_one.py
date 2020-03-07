from flask import Blueprint
from flask_restx import Api

from stats_service.version import VERSION
from stats_service.api.v1.stats import stats_namespace


def get_version_one_api():
    version_one_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
    api_version_one = Api(
        version_one_blueprint,
        doc="/doc",
        title="Stats Service",
        version=VERSION,
        description="Stats Service API",
    )

    api_version_one.add_namespace(stats_namespace)
    return version_one_blueprint
