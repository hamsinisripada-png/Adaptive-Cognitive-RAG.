import time
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import UTC, datetime


def utcnow() -> datetime:
    return datetime.now(UTC)


def utcnow_iso() -> str:
    return utcnow().isoformat()


class Stopwatch:
    def __init__(self) -> None:
        self._start: float | None = None
        self._elapsed: float = 0.0

    def start(self) -> "Stopwatch":
        self._start = time.perf_counter()
        return self

    def stop(self) -> float:
        if self._start is None:
            raise RuntimeError("Stopwatch was not started.")
        self._elapsed = time.perf_counter() - self._start
        self._start = None
        return self._elapsed

    @property
    def elapsed_seconds(self) -> float:
        return self._elapsed

    @property
    def elapsed_ms(self) -> float:
        return self._elapsed * 1000


@contextmanager
def timer() -> Iterator[Stopwatch]:
    sw = Stopwatch().start()
    try:
        yield sw
    finally:
        sw.stop()
