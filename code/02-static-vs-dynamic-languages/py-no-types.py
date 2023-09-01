class Motorcycle:

    def __init__(self, model, style, engine_size, off_road):
        self.off_road = off_road
        self.engine_size = engine_size
        self.style = style
        self.model = model

    @property
    def can_jump(self):
        return bool(self.off_road)

    def __str__(self):
        return (f'{self.model} {self.engine_size}, type: {self.style}, ' +
                f'off-road: {self.off_road}, can jump: {self.can_jump}')

    @classmethod
    def create_adventure(cls, model, engine_size):
        return Motorcycle(model, "Adventure", engine_size, True)


def create_bikes():
    motorcycles = [
        Motorcycle.create_adventure("Himalayan", 410),
        Motorcycle.create_adventure("Ténéré", 700),
        Motorcycle.create_adventure("KTM", 790),
        Motorcycle.create_adventure("Norden", 901),
    ]

    return motorcycles


if __name__ == '__main__':
    bikes = create_bikes()

    print("Here are some bikes!")
    for b in bikes:
        print(b)
        # Duck type: Motorcycles have a string model and a truthy can_jump.
        print(f'The {b.model} can{"" if b.can_jump else "NOT" } jump.')
