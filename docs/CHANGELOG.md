# Changelog

## Step 1 — Repository Initialization

- Initialized git repository.
- Created top-level directory structure: backend, frontend, docs, scripts, .github/workflows.
- Added .gitignore, LICENSE (MIT), root README.md.
- Added EditorConfig and base repository metadata files.

## Step 2 — Project Foundation

- `backend/pyproject.toml`: package metadata, runtime + dev dependencies, ruff/mypy/pytest config.
- `backend/.env.example`: full environment variable reference for every subsystem.
- `app/core/config.py`: `Settings` (pydantic-settings) with validated environment/log-level fields, `get_settings()` cached accessor.
- `app/core/constants.py`: shared string/path/enum constants.
- `app/core/logging.py`: structlog + stdlib logging integration, JSON in production, console in dev.
- `app/core/exceptions.py`: `AppError` hierarchy (NotFound, Validation, Conflict, Unauthorized, Forbidden, RateLimit, ServiceUnavailable, Internal).
- `app/core/error_handlers.py`: FastAPI exception handler registration producing structured `ErrorResponse` bodies.
- `app/core/di.py`: lightweight `Container` with singleton/factory providers, `get_container()`.
- `app/core/lifespan.py`: async app lifespan wiring logging, DI, telemetry startup/shutdown.
- `app/core/telemetry.py`: OpenTelemetry TracerProvider setup with optional OTLP/console exporters and FastAPI instrumentation.
- `app/core/metrics.py`: Prometheus `Counter`/`Histogram`/`Gauge` definitions on a dedicated registry.
- `app/middleware/request_id.py`: request ID generation/propagation via `X-Request-ID`.
- `app/middleware/logging.py`: structured request logging + Prometheus metric recording.
- `app/schemas/common.py`: `HealthResponse`, `VersionResponse`, `ErrorResponse`, `Pagination`, generic `PaginatedResponse`.
- `app/interfaces/base.py`: `Repository[T]`, `CacheBackend`, `Retriever`, `Embedder`, `Agent`, `HealthCheckable` protocols/ABCs.
- `app/utils/types.py`: `JSONScalar`/`JSONDict`/`JSONList`/`JSONValue` PEP 695 type aliases.
- `app/utils/time.py`: `utcnow`, `Stopwatch`, `timer` context manager.
- `app/api/health.py`, `app/api/version.py`, `app/api/metrics.py`: liveness, version metadata, Prometheus exposition endpoints.
- `app/main.py`: `create_app()` factory wiring CORS, middleware, exception handlers, routers; module-level `app`.
- Full `tests/` suite (health, version, metrics, config, exceptions) — 16 tests passing.
- Verified: `ruff check` clean, `mypy --strict` clean, `pytest` 16/16 passing, `uvicorn app.main:app` boots and serves `/health`, `/version`, `/metrics`.
