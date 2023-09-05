# ##########################################
#
# syntax of "x: type" *********************
#

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















