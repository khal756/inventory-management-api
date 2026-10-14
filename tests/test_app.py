
import pytest
from app import app, products
from unittest.mock import patch


@pytest.fixture
def client():
    # Reset products before each test
    products[:] = [
        {"id": 1, "name": "Milk", "price": 80, "quantity": 20},
        {"id": 2, "name": "Bread", "price": 65, "quantity": 10},
    ]

    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_get_products(client):
    response = client.get("/api/products")
    assert response.status_code == 200
    assert len(response.json) == 2


def test_add_product(client):
    response = client.post(
        "/api/products",
        json={"name": "Sugar", "price": 150, "quantity": 12}
    )
    assert response.status_code == 201
    assert response.json["name"] == "Sugar"


def test_update_product(client):
    response = client.patch(
        "/api/products/1",
        json={"quantity": 30}
    )
    assert response.status_code == 200
    assert response.json["quantity"] == 30


def test_delete_product(client):
    response = client.delete("/api/products/1")
    assert response.status_code == 200
    assert len(products) == 1


def test_product_not_found(client):
    response = client.delete("/api/products/999")
    assert response.status_code == 404



@patch("app.requests.get")
def test_import_external_product(mock_get, client):
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Test Chocolate",
            "brands": "Test Brand"
        }
    }
    mock_get.return_value.raise_for_status.return_value = None

    response = client.post("/api/import-product/123456789")

    assert response.status_code == 201
    assert response.json["product"]["name"] == "Test Chocolate"
    assert response.json["product"]["price"] == 0
    assert response.json["product"]["quantity"] == 0
