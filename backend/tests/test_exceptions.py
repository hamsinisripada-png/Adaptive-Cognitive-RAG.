from fastapi.testclient import TestClient

from app.core.exceptions import (
    ConflictError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
    ServiceUnavailableError,
    UnauthorizedError,
    ValidationError,
)


def test_not_found_error_defaults() -> None:
    err = NotFoundError()
    assert err.status_code == 404
    assert err.error_code == "not_found"
    assert err.message == "Resource not found."


def test_validation_error_carries_details() -> None:
    err = ValidationError("bad field", details={"field": "email"})
    assert err.status_code == 422
    assert err.details == {"field": "email"}


def test_conflict_unauthorized_forbidden_ratelimit_service_unavailable_codes() -> None:
    assert ConflictError().status_code == 409
    assert UnauthorizedError().status_code == 401
    assert ForbiddenError().status_code == 403
    assert RateLimitError().status_code == 429
    assert ServiceUnavailableError().status_code == 503


def test_unknown_route_returns_structured_error(client: TestClient) -> None:
    response = client.get("/this-route-does-not-exist")
    assert response.status_code == 404
    body = response.json()
    assert body["error"]["code"] == "http_error"
