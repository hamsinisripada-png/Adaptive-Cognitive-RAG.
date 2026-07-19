import platform

from fastapi import APIRouter, Depends

from app import __version__
from app.core.config import Settings, get_settings
from app.schemas.common import VersionResponse

router = APIRouter(tags=["system"])


@router.get("/version", response_model=VersionResponse, summary="Service version metadata")
async def version(settings: Settings = Depends(get_settings)) -> VersionResponse:
    return VersionResponse(
        name=settings.app_name,
        version=__version__,
        environment=settings.environment,
        python_version=platform.python_version(),
    )
