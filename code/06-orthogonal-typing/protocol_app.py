"""
# We COULD create an automobile base-class
# Wait, are motorcycles autos? or different?
# Well, we can drive both, that's good enough
# So it'll have engines, transmissions, key to turn on, throttle, brakes
# Wait, there are electric motorcycles and cars. I guess they still have transmissions (or do they?)
# Wait, there are off-road motorcycles, they don't have keys, but do have transmissions.
# Wait, we could drive a mech/robot thing too. But they have no keys, not throttle or brakes!
#         https://bostondynamics.com
# Ugh, OOP is hard. I just want something I can turn on, drive to a location/direction, and stop.
# Enter protocols!

"""

# ############################
#
#  Back to our motorcycle example from chapter 2, again
#


import enum
import random
import typing


# These should:
# turn_on
# turn_towards a direction
# accelerate at a rate

class Drivable(typing.Protocol):
    def turn_on(self) -> bool: ...

    def turn_towards(self, direction: str) -> None: ...

    def accelerate(self, rate: float) -> None: ...


def main():
    mc: Motorcycle = Motorcycle.create_adventure("Tènèrè", 700)
    do_vehicle_things(mc)


def do_vehicle_things(vehicle: Drivable):
    print("Doing vehicle things!")
    vehicle.turn_on()
    vehicle.turn_towards("North")
    vehicle.accelerate(9.81)


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
        self.model: str = model
        self.style: MotorcycleType = style
        self.engine_size: int = engine_size
        self.off_road: bool = off_road

    # Drivable protocol methods:

    def turn_on(self) -> bool:
        on = random.randint(0, 5) % 5 != 0
        print(f'The {self.model} is now {"running" if on else "stalled"}.')
        return on

    def turn_towards(self, direction: str) -> None:
        print(f'The {self.model} turns towards {direction}.')
        return

    def accelerate(self, rate: float) -> None:
        print(f'The {self.model} is now going {rate:,.2f} faster.')
        return

    @property
    def can_jump(self) -> bool:
        return self.off_road

    @classmethod
    def create_adventure(cls, model: str, engine_size: int) -> typing.Self:  # -> "Motorcycle" : # -> Motorcycle?
        bike = Motorcycle(model, MotorcycleType.adventure, engine_size, off_road=True)
        return bike

    def __str__(self) -> str:
        return (f'{self.model} {self.engine_size}, type: {self.style}, ' +
                f'off-road: {self.off_road}, can jump: {self.can_jump}')


if __name__ == '__main__':
    main()
