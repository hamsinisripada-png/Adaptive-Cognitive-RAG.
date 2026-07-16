from typing import Final

APP_TITLE: Final[str] = "Adaptive Cognitive RAG"
APP_DESCRIPTION: Final[str] = (
    "Production-grade retrieval intelligence platform combining hybrid search, "
    "knowledge graphs, multi-agent orchestration, memory, reflection, and "
    "confidence-scored evidence graphs."
)

DEFAULT_API_PREFIX: Final[str] = "/api/v1"

HEALTH_PATH: Final[str] = "/health"
VERSION_PATH: Final[str] = "/version"
METRICS_PATH: Final[str] = "/metrics"

REQUEST_ID_HEADER: Final[str] = "X-Request-ID"

ENVIRONMENT_DEVELOPMENT: Final[str] = "development"
ENVIRONMENT_STAGING: Final[str] = "staging"
ENVIRONMENT_PRODUCTION: Final[str] = "production"
ENVIRONMENT_TEST: Final[str] = "test"

VALID_ENVIRONMENTS: Final[frozenset[str]] = frozenset(
    {
        ENVIRONMENT_DEVELOPMENT,
        ENVIRONMENT_STAGING,
        ENVIRONMENT_PRODUCTION,
        ENVIRONMENT_TEST,
    }
)

DEFAULT_LOG_LEVEL: Final[str] = "INFO"
VALID_LOG_LEVELS: Final[frozenset[str]] = frozenset(
    {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
)
