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














