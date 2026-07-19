from fastapi import APIRouter

from app.schemas.common import HealthComponent, HealthResponse
from app.utils.time import utcnow

router = APIRouter(tags=["system"])


@router.get("/health", response_model=HealthResponse, summary="Liveness and readiness probe")
async def health() -> HealthResponse:
    components = [
        HealthComponent(name="api", status="ok", detail=None),
    ]
    overall = "ok" if all(c.status == "ok" for c in components) else "degraded"
    return HealthResponse(status=overall, timestamp=utcnow(), components=components)
