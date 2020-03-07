import marshmallow
import requests


from flask import request
from flask_restx import Namespace, Resource, fields, reqparse

from timeseries_service.config import STATS_SERVICE_URL
from timeseries_service.model.timeseries import TimeseriesSchema


timeseries_namespace = Namespace(
    "timeseries", description="Timeseries related operations", validate=True
)

timeseries_response_repr = timeseries_namespace.model(
    "Timeseries response",
    {
        "avg": fields.Float(
            required=True, description="Average of data points in range time"
        ),
        "sum": fields.Float(
            required=True, description=" Sum of data points in range time"
        )
    }
)


timeseries_parser_post = timeseries_namespace.parser()
timeseries_parser_post.add_argument(
    "name", location="json", required=True, help="Name of data point"
)
timeseries_parser_post.add_argument(
    "t", location="json", required=True, help="Timestamp as epoch"
)
timeseries_parser_post.add_argument("v", location="json",
                                    required=True, help="Value")


@timeseries_namespace.route("/")
class Timeseries(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("from", type=int,
                        required=True, help="Starting data point.")
    parser.add_argument("to", type=int,
                        required=True, help="Ending data point.")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base_url = "{stats_service_address}/api/v1/stats/".format(
            stats_service_address=STATS_SERVICE_URL
        )

        self.stats_api_session = requests.Session()

    @timeseries_namespace.doc(body=parser)
    @timeseries_namespace.marshal_with(timeseries_response_repr)
    def get(self):
        """
        Get average and sum statistics.
        """
        Timeseries.parser.parse_args()
        from_ = request.args.get("from")
        to = request.args.get("to")
        try:
            response = self.stats_api_session.get(
                f"{self.base_url}?from={from_}&to={to}",
                timeout=60,
                verify=False
            )
            response.raise_for_status()
            response_json = response.json()
        except requests.HTTPError:
            return {"error":
                    "Could not retrieve stats due to HTTP error"}, 400
        except ValueError:
            return {"error":
                    "Could not retrieve stats due to incorrect response"}, 400

        if response_json.get("avg") and response_json.get("sum"):
            return {"avg": response_json["avg"],
                    "sum": response_json["sum"]}, 200

        return {"error":
                "Could not retrieve stats due to incorrect response"}, 400

    def post(self):
        """
        Post timeseries data.
        """
        data = request.get_json()
        try:
            TimeseriesSchema(many=True).load(data["values"])
            return {}, 201
        except marshmallow.exceptions.ValidationError as e:
            return {"error": f"Something is wrong: {e}"}, 400
