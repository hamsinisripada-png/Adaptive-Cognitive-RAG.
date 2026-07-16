from typing import TYPE_CHECKING

from opentelemetry import trace
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

from app.core.config import Settings
from app.core.logging import get_logger

if TYPE_CHECKING:
    from fastapi import FastAPI

logger = get_logger(__name__)

_tracer_provider: TracerProvider | None = None


def setup_telemetry(app: "FastAPI", settings: Settings) -> None:
    global _tracer_provider

    if not settings.otel_traces_enabled:
        logger.info("telemetry_disabled")
        return

    resource = Resource.create(
        {
            SERVICE_NAME: settings.otel_service_name,
            "deployment.environment": settings.environment,
        }
    )
    provider = TracerProvider(resource=resource)

    if settings.otel_exporter_otlp_endpoint:
        try:
            from opentelemetry.exporter.otlp.proto.http.trace_exporter import (
                OTLPSpanExporter,
            )

            otlp_exporter = OTLPSpanExporter(
                endpoint=settings.otel_exporter_otlp_endpoint
            )
            provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
            logger.info(
                "telemetry_otlp_exporter_configured",
                endpoint=settings.otel_exporter_otlp_endpoint,
            )
        except Exception as exc:  # noqa: BLE001
            logger.warning("telemetry_otlp_exporter_failed", error=str(exc))

    if settings.otel_console_export:
        provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

    trace.set_tracer_provider(provider)
    _tracer_provider = provider

    try:
        from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

        FastAPIInstrumentor.instrument_app(app)
    except Exception as exc:  # noqa: BLE001
        logger.warning("telemetry_fastapi_instrumentation_failed", error=str(exc))

    logger.info("telemetry_initialized", service_name=settings.otel_service_name)


def shutdown_telemetry() -> None:
    global _tracer_provider
    if _tracer_provider is not None:
        _tracer_provider.shutdown()
        _tracer_provider = None
        logger.info("telemetry_shutdown")


def get_tracer(name: str = "app") -> trace.Tracer:
    return trace.get_tracer(name)
