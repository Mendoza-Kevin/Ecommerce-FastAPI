from fastapi.testclient import TestClient
import pytest
import os
import sys

# Get the location of the app folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient(app)

@pytest.fixture
def token_admin():
    response = client.post(
        "/api/v1/auth/login",
        data={
            "username": "admin@example.com",
            "password": "123"
        })
    assert response.status_code == 200
    return response.json()["access_token"]

def test_crear_producto_exitoso_admin(token_admin):
    response = client.post(
        "/api/v1/productos",
        headers= {
            "Authorization": f"Bearer {token_admin}"
        },
        json={
            "nombre": "Laptop Alienware",
            "precio": 1200,
            "stock": 6,
            "en_stock": True,
            "categoria_id": 1
        })
    assert response.status_code == 200

def test_crear_producto_sin_token():
    response = client.post(
        "/api/v1/productos",
        json={
            "nombre": "Audifonos Logitech",
            "precio": 30,
            "stock": 5,
            "en_stock": True,
            "categoria_id": 1
        })
    assert response.status_code == 401

def test_crear_producto_sin_nombre_admin(token_admin):
    response = client.post(
        "/api/v1/productos",
        headers= {
            "Authorization": f"Bearer {token_admin}"
        },
        json={
            "precio": 500,
            "stock": 10,
            "en_stock": True,
            "categoria_id": 1
        })
    assert response.status_code == 422

def test_listar_productos():
    response = client.get("/api/v1/productos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)