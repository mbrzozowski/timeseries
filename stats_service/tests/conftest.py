import pytest


from stats_service.__main__ import get_flask_app


@pytest.fixture
def app():
    app = get_flask_app()
    app.testing = True
    return app.test_client()
