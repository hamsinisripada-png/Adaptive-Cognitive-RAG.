from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from app.core.constants import (
    DEFAULT_API_PREFIX,
    DEFAULT_LOG_LEVEL,
    VALID_ENVIRONMENTS,
    VALID_LOG_LEVELS,
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="APP_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = Field(default="AC-RAG")
    environment: str = Field(default="development")
    debug: bool = Field(default=False)

    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000, ge=1, le=65535)
    api_prefix: str = Field(default=DEFAULT_API_PREFIX)

    log_level: str = Field(default=DEFAULT_LOG_LEVEL)
    log_json: bool = Field(default=False)

    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    secret_key: str = Field(default="change-me-in-production", min_length=8)

    otel_service_name: str = Field(default="ac-rag-backend")
    otel_exporter_otlp_endpoint: str | None = Field(default=None)
    otel_console_export: bool = Field(default=False)
    otel_traces_enabled: bool = Field(default=True)

    database_url: str = Field(
        default="postgresql+asyncpg://acrag:acrag@localhost:5432/acrag"
    )
    redis_url: str = Field(default="redis://localhost:6379/0")

    neo4j_uri: str = Field(default="bolt://localhost:7687")
    neo4j_user: str = Field(default="neo4j")
    neo4j_password: str = Field(default="neo4j_password")

    qdrant_url: str = Field(default="http://localhost:6333")
    qdrant_api_key: str | None = Field(default=None)

    @field_validator("environment", mode="before")
    @classmethod
    def validate_environment(cls, value: str) -> str:
        normalized = str(value).lower()
        if normalized not in VALID_ENVIRONMENTS:
            raise ValueError(f"Invalid environment: {value}")
        return normalized

    @field_validator("log_level", mode="before")
    @classmethod
    def validate_log_level(cls, value: str) -> str:
        upper = str(value).upper()
        if upper not in VALID_LOG_LEVELS:
            raise ValueError(f"Invalid log level: {value}")
        return upper

    @property
    def is_production(self) -> bool:
        return self.environment == "production"

    @property
    def is_development(self) -> bool:
        return self.environment == "development"

    @property
    def is_test(self) -> bool:
        return self.environment == "test"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
