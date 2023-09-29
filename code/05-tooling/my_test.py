from typing import Any, Final

x: str = "ABC"
z: Final[int] = 101


def print_a_number(num: int) -> list:
    print(num)
    another(1, 7)
    return None


def other(w):
    print(w.upper())


print_a_number(x)
print_a_number(z)
other(x)
other(z)

z = 102


def another(u, v) -> Any:
    return u + v
