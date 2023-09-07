# ##########################################
#
# Python allows for heterogeneous types all smushed together
#
import typing
from typing import Any


class Person:
    def __init__(self, name: str, number: int):
        self.name = name
        self.number = number


# Person.ssn = 434  # Naaaw

# Also, probably not:
things: list[Any] = [
    7,
    Person("Michael", 42),
    7.14,
    "Seven",
    "Seize the day!",
    [1, 1, 2, 3],
]

for t in things:
    print(t)

# Collections, the "right" way:
# from typing import List
# numbers: List[int] = [2, 3, 5, 7, 11, 13, 17, ]  # Works in 3.5+
numbers: list[int] = [2, 3, 5, 7, 11, 13, 17, ]  # 3.9+
people: list[Person] = [
    Person("Michael", 42),
    Person("Sarah", 3),
    Person("Zoe", 100),
]

print(numbers[0].to_bytes())  # Autocomplete
print(people[0].name)

# ##########################################
#
# More complex data structures:
#

user_lookup_by_id: dict[int, Person] = {
    p.number: p
    for p in people
}

u1 = user_lookup_by_id.get("Seven")  # <- Error, wrong key type
u2: str = user_lookup_by_id.get(42)  # <- Error, not a str.
print(u2)
u3 = user_lookup_by_id.get(3)
u4: Person = user_lookup_by_id.get(3)  # <- Bug, should be Optional[Person]

t: typing.Tuple[int, int, Person, str] = (7, 7, Person(1, 2), "")

def get_data() -> typing.Tuple[int, int, Person, str]:
    return 7, 7, Person(1, 2), ""


t2 = get_data()
# t2[2].name
