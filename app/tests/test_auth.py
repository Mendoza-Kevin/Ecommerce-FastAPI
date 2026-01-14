from fastapi.testclient import TestClient
import pytest
import os
import sys

# Get the location of the app folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

def test_login_invalido():
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "example@gmail.com",
            "password": "123"
        })
    assert response.status_code == 401

def test_ping_docs():
    response = client.get("/docs")
    assert response.status_code == 200

@pytest.fixture
def token():
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "brian@example.com",
            "password": "123"
        })
    assert response.status_code == 200
    return response.json()["access_token"]

def test_perfil_valido(token):
    response = client.get(
        "/api/v1/auth/usuarios/perfil",
        headers={
            "Authorization": f"Bearer {token}"
        })
    data = response.json()
    assert response.status_code == 200
    assert "email" in data
    assert "id" in data
    assert  "nombre" in data