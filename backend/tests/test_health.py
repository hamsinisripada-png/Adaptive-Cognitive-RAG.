from fastapi.testclient import TestClient


def test_health_returns_ok(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert "timestamp" in body
    assert isinstance(body["components"], list)
    assert body["components"][0]["name"] == "api"


def test_health_includes_request_id_header(client: TestClient) -> None:
    response = client.get("/health")
    assert "X-Request-ID" in response.headers


def test_health_respects_incoming_request_id(client: TestClient) -> None:
    response = client.get("/health", headers={"X-Request-ID": "abc-123"})
    assert response.headers["X-Request-ID"] == "abc-123"
