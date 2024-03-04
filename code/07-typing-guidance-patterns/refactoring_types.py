from motorbike import MotorBike


def create_some_bikes() -> list[MotorBike]:
    motorcycles = [
        MotorBike.create_adventure("Himalayan", 410),
        MotorBike.create_adventure("Tenere", 700),
        MotorBike.create_adventure("KTM", 790),
        MotorBike.create_adventure("Norden", 901),
    ]

    return motorcycles


if __name__ == '__main__':

    print("Some bikes: ")
    bikes = create_some_bikes()
    for b in bikes:
        print(b)
