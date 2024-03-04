from bike import Bike


def create_some_bikes() -> list[Bike]:
    motorcycles = [
        Bike.create_adventure("Himalayan", 410),
        Bike.create_adventure("Tenere", 700),
        Bike.create_adventure("KTM", 790),
        Bike.create_adventure("Norden", 901),
    ]

    return motorcycles


if __name__ == '__main__':

    print("Some bikes: ")
    bikes = create_some_bikes()
    for b in bikes:
        print(b)
