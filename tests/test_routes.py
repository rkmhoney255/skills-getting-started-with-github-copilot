def test_root_redirects_to_index_html(client):
    # Arrange: `client` fixture provided by conftest

    # Act: request root without following redirects
    response = client.get("/", follow_redirects=False)

    # Assert: redirect to static index.html
    assert response.status_code in (301, 302, 307)
    assert "/static/index.html" in response.headers.get("location", "")


def test_get_activities_returns_all_activities(client):
    # Arrange: client fixture

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, dict)
    # Known activity from the app
    assert "Chess Club" in body
