def test_smoke():
    """Check if pytest is working."""
    from timeseries_service.__main__ import main

    assert main is not None
