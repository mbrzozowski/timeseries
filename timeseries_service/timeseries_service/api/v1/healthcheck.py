from flask_restx import Namespace, Resource, fields

health_namespace = Namespace("health",
                             description="Health check related operations")

health_response_repr = health_namespace.model(
    "Health",
    {"status": fields.String(required=True,
                             description="Status of the service")}
)


@health_namespace.route("/")
class Health(Resource):
    @health_namespace.marshal_with(health_response_repr)
    def get(self):
        """
        Health check service status.
        """
        return {"status": "OK"}, 200
