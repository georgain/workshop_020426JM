from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_post_suma() -> None:
    response = client.post("/suma", json={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_post_resta() -> None:
    response = client.post("/resta", json={"a": 5, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 2}


def test_post_multiplicacion() -> None:
    response = client.post("/multiplicacion", json={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 6}
