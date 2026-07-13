from typing import TYPE_CHECKING

from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.core.constants import REQUEST_ID_HEADER
from app.core.exceptions import AppError
from app.core.logging import get_logger
from app.schemas.common import ErrorDetail, ErrorResponse

if TYPE_CHECKING:
    from fastapi import FastAPI

logger = get_logger(__name__)


def _request_id(request: Request) -> str | None:
    return request.headers.get(REQUEST_ID_HEADER) or getattr(
        request.state, "request_id", None
    )


async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    logger.warning(
        "app_error",
        error_code=exc.error_code,
        message=exc.message,
        path=request.url.path,
    )
    body = ErrorResponse(
        error=ErrorDetail(code=exc.error_code, message=exc.message, details=exc.details),
        request_id=_request_id(request),
    )
    return JSONResponse(status_code=exc.status_code, content=body.model_dump(mode="json"))


async def http_exception_handler(
    request: Request, exc: StarletteHTTPException
) -> JSONResponse:
    body = ErrorResponse(
        error=ErrorDetail(code="http_error", message=str(exc.detail)),
        request_id=_request_id(request),
    )
    return JSONResponse(status_code=exc.status_code, content=body.model_dump(mode="json"))


async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    body = ErrorResponse(
        error=ErrorDetail(
            code="validation_error",
            message="Request validation failed.",
            details={"errors": exc.errors()},
        ),
        request_id=_request_id(request),
    )
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=body.model_dump(mode="json"),
    )


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.error(
        "unhandled_exception",
        error=str(exc),
        error_type=type(exc).__name__,
        path=request.url.path,
        exc_info=True,
    )
    body = ErrorResponse(
        error=ErrorDetail(code="internal_error", message="An unexpected error occurred."),
        request_id=_request_id(request),
    )
    return JSONResponse(status_code=500, content=body.model_dump(mode="json"))


def register_exception_handlers(app: "FastAPI") -> None:
    app.add_exception_handler(AppError, app_error_handler)  # type: ignore[arg-type]
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(Exception, unhandled_exception_handler)
