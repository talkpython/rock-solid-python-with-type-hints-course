import enum
import typing


class MotorcycleType(enum.StrEnum):
    sport = "sport"
    naked = "naked"
    touring = "touring"
    adventure = "adventure"
    dual_sport = "dual_sport"
    motocross = "motocross"
    cross_country = "cross_country"
    trail = "trail"


class Motorcycle:

    def __init__(self, model: str, style: MotorcycleType, engine_size: int, off_road: bool):
        self.off_road: bool = off_road
        self.engine_size: int = engine_size
        self.style: MotorcycleType = style
        self.model: str = model

    @property
    def can_jump(self) -> bool:
        return bool(self.off_road)

    def __str__(self) -> str:
        return (f'{self.model} {self.engine_size}, type: {self.style}, ' +
                f'off-road: {self.off_road}, can jump: {self.can_jump}')

    @classmethod
    def create_adventure(cls, model, engine_size) -> typing.Self:
        return Motorcycle(model, MotorcycleType.adventure, engine_size, True)


def create_bikes() -> list[Motorcycle]:
    motorcycles = [
        Motorcycle.create_adventure("Himalayan", 410),
        Motorcycle.create_adventure("Ténéré", 700),
        Motorcycle.create_adventure("KTM", 790),
        Motorcycle.create_adventure("Norden", 901),
    ]

    return motorcycles


if __name__ == '__main__':
    bikes: list[Motorcycle] = create_bikes()

    print("Here are some bikes!")
    for b in bikes:
        print(b)
        # Duck type: Motorcycles have a string model and a truthy can_jump.
        print(f'The {b.model} can{"" if b.can_jump else "NOT"} jump.')
