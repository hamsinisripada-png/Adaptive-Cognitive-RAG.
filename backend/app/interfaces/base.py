from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

from app.utils.types import JSONDict


class Repository[T](ABC):
    @abstractmethod
    async def get(self, entity_id: str) -> T | None: ...

    @abstractmethod
    async def list(self, *, limit: int = 100, offset: int = 0) -> list[T]: ...

    @abstractmethod
    async def create(self, entity: T) -> T: ...

    @abstractmethod
    async def update(self, entity_id: str, entity: T) -> T | None: ...

    @abstractmethod
    async def delete(self, entity_id: str) -> bool: ...


@runtime_checkable
class CacheBackend(Protocol):
    async def get(self, key: str) -> str | None: ...

    async def set(self, key: str, value: str, *, ttl_seconds: int | None = None) -> None: ...

    async def delete(self, key: str) -> None: ...

    async def exists(self, key: str) -> bool: ...


@runtime_checkable
class Retriever(Protocol):
    async def retrieve(self, query: str, *, top_k: int = 10) -> list[JSONDict]: ...


@runtime_checkable
class Embedder(Protocol):
    async def embed(self, texts: list[str]) -> list[list[float]]: ...

    @property
    def dimensions(self) -> int: ...


@runtime_checkable
class Agent(Protocol):
    name: str

    async def run(self, state: JSONDict) -> JSONDict: ...


@runtime_checkable
class HealthCheckable(Protocol):
    name: str

    async def check_health(self) -> tuple[bool, str | None]: ...
