def test_health_should_return_ok(app):
    """
    Health endpoint should return OK status.
    """
    response = app.get("/api/v1/health/")

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == {'status': 'OK'}
