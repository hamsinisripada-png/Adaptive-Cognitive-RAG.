from fastapi.testclient import TestClient

from app import __version__


def test_version_returns_metadata(client: TestClient) -> None:
    response = client.get("/version")
    assert response.status_code == 200
    body = response.json()
    assert body["version"] == __version__
    assert body["environment"] == "test"
    assert "python_version" in body
    assert body["name"]
