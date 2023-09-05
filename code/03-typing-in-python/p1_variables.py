# ##########################################
#
# syntax of "x: type" *********************
#
import typing
from typing import Optional

x = 7
y: int = 10  # Explicitly declare the type as int.

print(x, y)  # Just to clear the editor warnings.

x = "Happy numbers"
y = "Sad numbers"  # Error in the editor.

print(x, y)

# ##########################################
#
# Survey of core types *********************
#

u: int = 27
v: float = 1.4121356
c: complex = complex(0, -v)
text: str = "Some text"
b: bytes = b"Bytes text"
truth: bool = True
lst: list = [1, 1, 2, 3, 5, 8]
s: set = {1, 1, 2, 3, 5, 8}  # 1,2,3,5,8

print(u, v, c, text, b, truth, lst, s)

lst = s  # <- Error

# ##########################################
#
# Nullable types *********************
#

z: int = 42
print(z)

z = None  # <- Error!

z2: str = "Never nothing!"
print(z2)
z2 = None  # <- Error!

z3: typing.Optional[int] = 43
print(z3)
z3: Optional[int] = 43
z4: int | None = 43
print(z3)
z3 = None
print(z3)
z3 = 44
print(z3)
z3 = "ABC"  # <- Error!

# ##########################################
#
# Unions *********************
#

un1: typing.Union[int, str] = 1
un2: int | str = 2
un3: int | str = "Three"

print(un1 + un2)

un1 = "One"
un2 = "Two"
print(un1 + un2)

un1 = [1, 1, 2]  # <- Error!

# un1.casefold()

# ##########################################
#
# What if you don't know the type? *********
#

unknown: typing.Any = 78
# unknown: Any = 78
print(unknown)

unknown = "Seventy Eight!"
print(unknown)

unknown = {7, 8, 8}
print(unknown)

# ##########################################
#
# Constants *********************
#

not_const_1 = "Some value"
print(not_const_1)

not_const_1 = "Other value"

CONST_2 = "Fixed value"  # Implicit, conventional constant
print(CONST_2)
CONST_2 = "No longer fixed!"  # Should have a warning, I guess?

CONST_3: typing.Final = "Really a constant, sorta"  # Explicit constant in the type system.
print(CONST_3)

CONST_3 = "This should not change!"  # <- Error! In the type system.
print(CONST_3)

# ##########################################
#
# Beware Little Bobby Tables ****************
# https://peps.python.org/pep-0675/
#

# Old way:
# student_name: str = input("What is the student's name?")
# student_name: str = "Robert Tables"
# query: str = f"SELECT * FROM Students WHERE name ='{student_name}'"
# print(query)
#
# student_name = "'; DROP TABLE Students; --"
# query = f"SELECT * FROM Students WHERE name ='{student_name}'"
# print(query)

# New way:
# student_name: str = input("What is the student's name?")
student_name: typing.LiteralString = "Robert Tables"
query: typing.LiteralString = f"SELECT * FROM Students WHERE name ='{student_name}'"
print(query)

student_name = "'; DROP TABLE Students; --"
query = f"SELECT * FROM Students WHERE name ='{student_name}'"
print(query)















