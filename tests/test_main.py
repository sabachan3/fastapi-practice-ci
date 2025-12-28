from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_add_ok():
    r = client.post("/add", json={"a": 3, "b": 5})
    assert r.status_code == 200
    assert r.json() == {"result": 8}


def test_add_out_of_range_422():
    r = client.post("/add", json={"a": 1_000_001, "b": 0})
    assert r.status_code == 422
