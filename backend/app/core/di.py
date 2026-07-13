from collections.abc import Callable
from functools import lru_cache
from typing import Any, TypeVar

from app.core.config import Settings, get_settings
from app.core.logging import get_logger

T = TypeVar("T")


class Container:
    """Lightweight dependency injection container.

    Providers are registered as zero-argument factories and resolved lazily.
    Singleton providers are memoized on first resolution.
    """

    def __init__(self, settings: Settings | None = None) -> None:
        self._settings = settings or get_settings()
        self._singletons: dict[str, Any] = {}
        self._factories: dict[str, Callable[[], Any]] = {}
        self._register_defaults()

    def _register_defaults(self) -> None:
        self.register_singleton("settings", lambda: self._settings)
        self.register_singleton("logger", lambda: get_logger("app"))

    def register_singleton(self, key: str, factory: Callable[[], Any]) -> None:
        self._factories[key] = factory

    def register_factory(self, key: str, factory: Callable[[], Any]) -> None:
        self._factories[key] = factory
        self._singletons.pop(key, None)

    def resolve(self, key: str) -> Any:
        if key in self._singletons:
            return self._singletons[key]
        if key not in self._factories:
            raise KeyError(f"No provider registered for '{key}'")
        instance = self._factories[key]()
        self._singletons[key] = instance
        return instance

    def override(self, key: str, instance: Any) -> None:
        self._singletons[key] = instance

    def reset(self, key: str | None = None) -> None:
        if key is None:
            self._singletons.clear()
        else:
            self._singletons.pop(key, None)

    @property
    def settings(self) -> Settings:
        return self.resolve("settings")  # type: ignore[no-any-return]


@lru_cache(maxsize=1)
def get_container() -> Container:
    return Container()
