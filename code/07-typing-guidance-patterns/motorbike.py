import enum
import typing


class BikeType(enum.StrEnum):
    sport = "sport"
    naked = "naked"
    touring = "touring"
    adventure = "adventure"
    dual_sport = "dual_sport"
    motocross = "motocross"
    cross_country = "cross_country"
    trail = "trail"


class MotorBike:

    def __init__(self, model: str, style: BikeType, engine_size: int, off_road: bool):
        self.model: str = model
        self.style: BikeType = style
        self.engine_size: int = engine_size
        self.off_road: bool = off_road

    @property
    def can_jump(self) -> bool:
        return self.off_road

    @classmethod
    def create_adventure(cls, model: str, engine_size: int) -> typing.Self:  # -> Motorcycle?
        bike = MotorBike(model, BikeType.adventure, engine_size, off_road=True)
        return bike

    def __str__(self) -> str:
        return (f'{self.model} {self.engine_size}, type: {self.style}, ' +
                f'off-road: {self.off_road}, can jump: {self.can_jump}')
