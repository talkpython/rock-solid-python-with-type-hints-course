import fastapi

from api.models.stats_model import StatsModel
from services import package_service, user_service

router = fastapi.APIRouter()


@router.get('/api/stats', response_model=StatsModel)
async def stats():
    packages = await package_service.package_count()
    releases = await package_service.release_count()
    users = await user_service.user_count()

    model = StatsModel(user_count=users, package_count=packages, release_count=releases)
    return model
