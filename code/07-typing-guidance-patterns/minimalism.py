from typing import Iterable


def main():
    nums = [1, 1, 2, 3, 5]
    func(nums)

    nums2 = (1, 1, 2, 3, 5)
    func(nums2)

    nums3 = (n * n for n in nums)
    func(nums3)


def func(things: Iterable[int]):
    print(type(things))
    for t in things:
        print(f'{t}^2 = {t * t:,}', end=', ')
    print()


def func_cluttered(things: list[int]):
    print(type(things))
    for t in things:
        print(f'{t}^2 = {t * t:,}', end=', ')
    print()


if __name__ == '__main__':
    main()
