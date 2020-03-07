def test_stats_should_return_bad_request(app):
    """
    Endpoint should return Bad request when parameters
    are missing.
    """
    response = app.get("/api/v1/stats/")

    assert response.status_code == 400


def test_stats_should_return_ok(app, mocker):
    """
    Endpoint should return 200 when parameters are taken from db.
    """
    mocker.patch("stats_service.model.timeseries.TimeseriesModel."
                 "calculate_avg_by_time_range", return_value=(2.33,))
    mocker.patch("stats_service.model.timeseries.TimeseriesModel."
                 "calculate_sum_by_time_range", return_value=(7.0,))

    response = app.get("/api/v1/stats/?from=4&to=6")

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.json == {'avg': 2.33, 'sum': 7.0}
