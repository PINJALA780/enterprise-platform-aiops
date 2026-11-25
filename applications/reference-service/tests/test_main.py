import pytest

from fastapi.testclient import TestClient

from app.main import app, orders


client = TestClient(app)


@pytest.fixture(autouse=True)
def clean_orders():

    orders.clear()

    yield

    orders.clear()


def test_root_endpoint():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["service"] == (
        "enterprise-reference-service"
    )


def test_health_endpoint():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_readiness_endpoint():

    response = client.get("/ready")

    assert response.status_code == 200

    assert response.json()["status"] == "ready"


def test_create_order():

    payload = {
        "customer_id": "CUST-1001",
        "product_name": "Laptop",
        "quantity": 2
    }

    response = client.post(
        "/api/v1/orders",
        json=payload
    )

    assert response.status_code == 201

    assert response.json()["customer_id"] == "CUST-1001"

    assert response.json()["quantity"] == 2

    assert "order_id" in response.json()


def test_get_orders():

    client.post(
        "/api/v1/orders",
        json={
            "customer_id": "CUST-1001",
            "product_name": "Laptop",
            "quantity": 2
        }
    )

    response = client.get("/api/v1/orders")

    assert response.status_code == 200

    assert response.json()["count"] == 1


def test_order_not_found():

    response = client.get(
        "/api/v1/orders/invalid-order-id"
    )

    assert response.status_code == 404


def test_invalid_order_quantity():

    response = client.post(
        "/api/v1/orders",
        json={
            "customer_id": "CUST-1001",
            "product_name": "Laptop",
            "quantity": 0
        }
    )

    assert response.status_code == 422


def test_request_id_header():

    response = client.get("/health")

    assert response.status_code == 200

    assert "X-Request-ID" in response.headers

    assert len(response.headers["X-Request-ID"]) == 36
