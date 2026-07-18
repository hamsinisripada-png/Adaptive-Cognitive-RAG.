import pytest
from pydantic import ValidationError

from app.core.config import Settings

_ENV_KEYS = (
    "APP_ENVIRONMENT",
    "APP_LOG_LEVEL",
    "APP_DEBUG",
    "APP_APP_NAME",
    "APP_PORT",
    "APP_SECRET_KEY",
)


@pytest.fixture(autouse=True)
def _isolated_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in _ENV_KEYS:
        monkeypatch.delenv(key, raising=False)


def test_default_settings_load() -> None:
    settings = Settings(_env_file=None)
    assert settings.app_name == "AC-RAG"
    assert settings.environment == "development"
    assert settings.port == 8000


def test_invalid_environment_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(_env_file=None, environment="not-a-real-env")


def test_invalid_log_level_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(_env_file=None, log_level="VERBOSE")


def test_log_level_normalized_to_uppercase() -> None:
    settings = Settings(_env_file=None, log_level="debug")
    assert settings.log_level == "DEBUG"


def test_environment_flags() -> None:
    assert Settings(_env_file=None, environment="production").is_production
    assert Settings(_env_file=None, environment="development").is_development
    assert Settings(_env_file=None, environment="test").is_test


def test_secret_key_minimum_length_enforced() -> None:
    with pytest.raises(ValidationError):
        Settings(_env_file=None, secret_key="short")
