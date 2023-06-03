# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_data():
    data = {"key": "value"}
    response = client.post("/data", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Data created successfully"}
