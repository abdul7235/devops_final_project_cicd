import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_random_file_with_checksum():
    response = client.get("/generate_random_file_with_checksum/")
    assert response.status_code == 200
    response_data = response.json()
    assert "file" in response_data
    assert "checksum" in response_data
    assert isinstance(response_data["file"], str)
    assert isinstance(response_data["checksum"], str)

