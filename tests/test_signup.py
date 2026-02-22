from src import app as app_module


def test_signup_adds_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "new_student@example.com"
    assert email not in app_module.activities[activity]["participants"]

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert email in app_module.activities[activity]["participants"]
    assert "Signed up" in response.json().get("message", "")


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    existing = app_module.activities[activity]["participants"][0]

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": existing})

    # Assert
    assert response.status_code == 400


def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Activity"
    email = "someone@example.com"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404


def test_unregister_removes_participant(client):
    # Arrange
    activity = "Chess Club"
    email = app_module.activities[activity]["participants"][0]
    assert email in app_module.activities[activity]["participants"]

    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert email not in app_module.activities[activity]["participants"]


def test_unregister_when_not_signed_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "not-signed@example.com"

    # Act
    response = client.post(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 400
