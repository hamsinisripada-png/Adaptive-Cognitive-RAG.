import time
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING

from app.core.config import get_settings
from app.core.di import get_container
from app.core.logging import configure_logging, get_logger
from app.core.telemetry import setup_telemetry, shutdown_telemetry

if TYPE_CHECKING:
    from fastapi import FastAPI

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: "FastAPI") -> AsyncIterator[None]:
    settings = get_settings()
    configure_logging(settings)
    container = get_container()
    app.state.container = container
    app.state.settings = settings
    app.state.started_at = time.time()

    setup_telemetry(app, settings)

    logger.info(
        "app_startup",
        environment=settings.environment,
        app_name=settings.app_name,
    )

    try:
        yield
    finally:
        logger.info("app_shutdown")
        shutdown_telemetry()
