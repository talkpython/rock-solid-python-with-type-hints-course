import beanie


class ReleaseAnalytics(beanie.Document):
    total_releases: int

    class Settings:
        name = 'release_analytics'
        indexes = []
