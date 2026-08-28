from app import create_app


def test_home_route():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "CloudOps Platform"
    assert data["status"] == "healthy"


def test_health_route():
    app = create_app()
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"
