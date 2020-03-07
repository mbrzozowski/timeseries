from flask import request
from flask_restx import Namespace, Resource, fields, reqparse
from stats_service.model.timeseries import TimeseriesModel


stats_namespace = Namespace(
    "stats", description="Stats related operations", validate=True
)

stats_response_repr = stats_namespace.model(
    "Stats response",
    {
        "avg": fields.Float(
            required=True, description="Average of data points in range time"
        ),
        "sum": fields.Float(
            required=True, description=" Sum of data points in range time"
        ),
    },
)


@stats_namespace.route("/")
class Stats(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("from",
                        type=int,
                        required=True,
                        help="Starting data point.")
    parser.add_argument("to",
                        type=int,
                        required=True,
                        help="Ending data point.")

    @stats_namespace.doc(body=parser)
    @stats_namespace.marshal_with(stats_response_repr)
    def get(self):
        """
        Get average and sum statistics.
        """
        Stats.parser.parse_args()
        from_ = request.args.get("from")
        to = request.args.get("to")
        su = TimeseriesModel.calculate_sum_by_time_range(from_, to)
        avg = TimeseriesModel.calculate_avg_by_time_range(from_, to)
        if su and avg and su != "null" and avg != "null":
            return {"avg": avg[0], "sum": su[0]}, 200
        return {"error": "something is wrong"}, 500
