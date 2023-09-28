import fastapi

from api.models.recent_package_model import RecentPackagesModel, RecentPackage
from models.package import Package
from services import package_service

router = fastapi.APIRouter()


@router.get('/api/packages/recent/{count}', response_model=RecentPackagesModel)
async def recent(count: int):
    count = max(1, count)
    packages = await package_service.recently_updated(count)

    package_models = [
        RecentPackage(name=p.id, updated=p.last_updated)
        for p in packages
    ]

    model = RecentPackagesModel(count=count, packages=package_models)
    return model


@router.get('/api/packages/details/{name}', response_model=Package)
async def details(name: str):
    package = await package_service.package_by_name(name)
    if package is None:
        return fastapi.responses.JSONResponse({'error': f'Package {name} not found'}, status_code=404)

    return package
