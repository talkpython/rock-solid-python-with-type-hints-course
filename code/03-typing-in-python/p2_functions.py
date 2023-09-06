import typing
from typing import Optional


def main():
    print("Typing functions")
    print()

    n1 = fib(1)
    n2 = fib(2)
    n3 = fib(3)
    n4 = fib(4)

    print(n1, n2, n3, n4)

    o1 = fib_small(-1)
    o2 = fib_small(5)
    print(o1, o2)

    say_hello("Michael")
    x = say_hello("Sam")
    print(type(x), x)

    use_function_explicit(lambda p1, p2: print(f"{p1}'s favorite number is {p2}."))
    # use_function(lambda a: a*a)  # <- Error and a crash.
    use_function_explicit(usable_func1)
    # use_function_explicit(usable_func2)  # <- Error and a crash.


def usable_func1(name: str, num: int) -> None:
    print(f"{name}'s common number is {num}.")


def usable_func2(name: str) -> None:
    print(f"Hello {name}")


def use_function_explicit(f: typing.Callable[[str, int], None]):
    f("Michael", 42)


def use_function(f):
    f("Michael", 42)


def fib(n: int) -> int:
    current, nxt = 0, 1

    for _ in range(n):
        current, nxt = nxt, nxt + current

    return current


def fib_small(n: int) -> Optional[int]:
    if n <= 0:
        return None

    return fib(n)


def say_hello(name: str) -> None:
    print(f'Hello there {name}!')


if __name__ == '__main__':
    main()
