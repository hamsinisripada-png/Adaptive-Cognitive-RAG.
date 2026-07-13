from typing import Any


class AppError(Exception):
    status_code: int = 500
    error_code: str = "internal_error"

    def __init__(
        self,
        message: str = "An unexpected error occurred.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        self.message = message
        self.details = details or {}
        super().__init__(message)


class NotFoundError(AppError):
    status_code = 404
    error_code = "not_found"

    def __init__(
        self, message: str = "Resource not found.", *, details: dict[str, Any] | None = None
    ) -> None:
        super().__init__(message, details=details)


class ValidationError(AppError):
    status_code = 422
    error_code = "validation_error"

    def __init__(
        self, message: str = "Validation failed.", *, details: dict[str, Any] | None = None
    ) -> None:
        super().__init__(message, details=details)


class ConflictError(AppError):
    status_code = 409
    error_code = "conflict"

    def __init__(
        self,
        message: str = "Resource conflict.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, details=details)


class UnauthorizedError(AppError):
    status_code = 401
    error_code = "unauthorized"

    def __init__(
        self, message: str = "Authentication required.", *, details: dict[str, Any] | None = None
    ) -> None:
        super().__init__(message, details=details)


class ForbiddenError(AppError):
    status_code = 403
    error_code = "forbidden"

    def __init__(
        self, message: str = "Access denied.", *, details: dict[str, Any] | None = None
    ) -> None:
        super().__init__(message, details=details)


class RateLimitError(AppError):
    status_code = 429
    error_code = "rate_limited"

    def __init__(
        self,
        message: str = "Rate limit exceeded.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, details=details)


class ServiceUnavailableError(AppError):
    status_code = 503
    error_code = "service_unavailable"

    def __init__(
        self,
        message: str = "Upstream service unavailable.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, details=details)


class InternalError(AppError):
    status_code = 500
    error_code = "internal_error"

    def __init__(
        self,
        message: str = "An unexpected error occurred.",
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message, details=details)
