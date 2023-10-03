import math

from beartype import beartype

from timd import timed_function


def main():
    totals = collector_top([100, 20, 60])
    print(f"Done with {totals:,} actions.")


@timed_function
def collector_top(counts: list[int]) -> int:
    total: int = 1

    for count in counts:
        for _ in range(count):
            total += collect_part1(int(count / 5))
            total += collect_part2(int(count / 2))

    return total


@beartype
def collect_part1(count: int) -> int:
    total: int = 0
    groups = []

    for _ in range(count):
        total += 1
        math_stuff(count, groups)

    return total


@beartype
def math_stuff(count: int, groups: list[float]):
    for _ in range(10_000):
        groups.append(math.sqrt(count))


@beartype
def collect_part2(count: int) -> int:
    total: int = 1
    groups = []
    str_stuff(groups)

    return total


@beartype
def str_stuff(groups: list[str]):
    for _ in range(10_000):
        groups.append("This is a common sentence. " * 100)


if __name__ == '__main__':
    main()
