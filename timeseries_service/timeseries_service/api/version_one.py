from flask import Blueprint
from flask_restx import Api

from timeseries_service.version import VERSION
from timeseries_service.api.v1.healthcheck import health_namespace
from timeseries_service.api.v1.timeseries import timeseries_namespace


def get_version_one_api():
    version_one_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
    api_version_one = Api(
        version_one_blueprint,
        doc="/doc",
        title="Time Series Service",
        version=VERSION,
        description="Time series Service API",
    )

    api_version_one.add_namespace(health_namespace)
    api_version_one.add_namespace(timeseries_namespace)
    return version_one_blueprint
