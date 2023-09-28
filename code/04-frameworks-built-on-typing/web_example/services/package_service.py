import datetime
from typing import Optional

import pymongo.results
from beanie.odm.operators.find.array import ElemMatch
from beanie.odm.operators.update import array
from beanie.odm.operators.update.general import Set, Inc

from models.package import Package, Release, PackageTopLevelOnly
from models.release_analytics import ReleaseAnalytics


async def package_count() -> int:
    return await Package.count()


async def release_count() -> int:
    analytics = await ReleaseAnalytics.find_one()
    if not analytics:
        print("ERROR: No analytics?")
        return 0

    return analytics.total_releases


async def recently_updated(count: int = 5) -> list[Package]:
    # noinspection PyUnresolvedReferences
    updated = await Package.find_all().sort(-Package.last_updated).limit(count).to_list()

    return updated


async def package_by_name(name: str, summary_only=False) -> Optional[Package] | Optional[PackageTopLevelOnly]:
    if not name:
        return None

    name = name.lower().strip()

    query = Package.find_one(Package.id == name)

    if not summary_only:
        return await query
    else:
        return await query.project(PackageTopLevelOnly)


async def packages_with_version(major: int, minor: int, build: int) -> int:
    # noinspection PyUnresolvedReferences
    # Oops, not exactly!
    # packages_count = await Package.find(
    #     Package.releases.major_ver == major,# 1
    #     Package.releases.minor_ver == minor,# 2
    #     Package.releases.build_ver == build,
    # ).count()

    packages_count = await Package.find(
        ElemMatch(
            Package.releases,
            {"major_ver": major, "minor_ver": minor, "build_ver": build}
        )
    ).count()

    return packages_count


async def create_release(major: int, minor: int, build: int,
                         name: str, comment: str, size: int, url: Optional[str]):
    release = Release(
        major_ver=major, minor_ver=minor, build_ver=build,
        comment=comment, url=url, size=size
    )

    update_result: pymongo.results.UpdateResult = await Package \
        .find_one(Package.id == name).update(
        array.Push({Package.releases: release}),
        Set({Package.last_updated: datetime.datetime.now()})
    )

    if update_result.modified_count < 1:
        raise Exception(f"No package with {name}")

    await ReleaseAnalytics.find_one().update(Inc({ReleaseAnalytics.total_releases: 1}))

# Fine but full ODM style, less efficient
# async def create_release(major: int, minor: int, build: int,
#                          name: str, comment: str, size: int, url: Optional[str]):
#     package = await package_by_name(name)
#     if package is None:
#         raise Exception(f"No package with {name}")
#
#     release = Release(
#         major_ver=major, minor_ver=minor, build_ver=build,
#         comment=comment, url=url, size=size
#     )
#
#     package.last_updated = datetime.datetime.now()
#     package.releases.append(release)
#     await package.save()
#
#     analytics = await ReleaseAnalytics.find_one()
#     analytics.total_releases += 1
#     await analytics.save()
