from beartype import beartype


class Point:
    def __init__(self, value: float):
        self.value = value


def main():
    # x = input("Enter the first number: ")
    # y = input("Enter the second number: ")
    x: float = float(input("Enter the first number: "))
    y: float = float(input("Enter the second number: "))

    z = math_on_numbers(x, y)
    print(f"The result is {z}.")

    p1 = Point(x)
    p2 = Point(y)
    z = math_on_points(p1, p2)
    # z = math_on_points(p1, y)
    print(f"The result is {z}.")


@beartype
def math_on_numbers(x: float, y: float):
    return x * x + 3 * y


@beartype
def math_on_points(x: Point, y: Point):
    return x.value * x.value + 3 * y.value


if __name__ == '__main__':
    main()
