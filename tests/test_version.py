from .context import anon_client


def test_version(anon_client):
    """Test the version string.

    :api_client: injected by pytest
    """
    response = anon_client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.1.0-alpha"}
