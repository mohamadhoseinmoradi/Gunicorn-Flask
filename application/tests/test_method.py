from wsgi import app


def test_app_route_response():
    response = app.test_client().get("/tree")
    assert response.status_code == 200
