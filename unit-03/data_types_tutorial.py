"""
Python Data Types and Data Structures Tutorial
Based on CPRG-217 Unit 03 Slides

This tutorial covers:
- Built-in data types in Python
- The type() function
- Data structures: Lists, Tuples, Dictionaries, and Sets
"""

# =============================================================================
# SECTION 1: Introduction to Data Types
# =============================================================================
print("=" * 70)
print("SECTION 1: Introduction to Data Types")
print("=" * 70)

# Python is dynamically typed - you don't need to declare types explicitly
x = 10  # x is an integer
print(f"x = {x}")
print(f"Type of x: {type(x)}")

x = "Hello"  # Now x is a string
print(f"x = {x}")
print(f"Type of x: {type(x)}")
print()

# =============================================================================
# SECTION 2: The type() Function
# =============================================================================
print("=" * 70)
print("SECTION 2: The type() Function")
print("=" * 70)

# Using type() to determine data types
a = 10
print(f"a = {a}, type: {type(a)}")  # <class 'int'>

b = 3.14
print(f"b = {b}, type: {type(b)}")  # <class 'float'>

c = {"Alice": 1, "in": 2, "Wonderland": 3}
print(f"c = {c}, type: {type(c)}")  # <class 'dict'>

d = ("Alice", "in", "Wonderland")
print(f"d = {d}, type: {type(d)}")  # <class 'tuple'>

x = True
print(f"x = {x}, type: {type(x)}")  # <class 'bool'>

y = "hello"
print(f"y = {y}, type: {type(y)}")  # <class 'str'>

z = [1, 2, 3]
print(f"z = {z}, type: {type(z)}")  # <class 'list'>
print()

# =============================================================================
# SECTION 3: Numeric Data Types
# =============================================================================
print("=" * 70)
print("SECTION 3: Numeric Data Types")
print("=" * 70)

# Integer
integer_num = 42
print(f"Integer: {integer_num}, type: {type(integer_num)}")

# Float
float_num = 3.14159
print(f"Float: {float_num}, type: {type(float_num)}")

# Complex
complex_num = 3 + 4j
print(f"Complex: {complex_num}, type: {type(complex_num)}")
print()

# =============================================================================
# SECTION 4: Lists - Ordered, Mutable Collections
# =============================================================================
print("=" * 70)
print("SECTION 4: Lists")
print("=" * 70)

# Create a list of fruits
fruits = ["apple", "banana", "cherry"]
print(f"Original list: {fruits}")

# Access elements in the list (indexing starts at 0)
print(f"First fruit: {fruits[0]}")  # apple
print(f"Second fruit: {fruits[1]}")  # banana

# Add a new fruit to the list
fruits.append("orange")
print(f"After append: {fruits}")

# Remove a fruit from the list
fruits.remove("banana")
print(f"After remove: {fruits}")

# Other useful list operations
print(f"Length of list: {len(fruits)}")
print(f"Last element: {fruits[-1]}")
print()

# =============================================================================
# SECTION 5: Tuples - Ordered, Immutable Collections
# =============================================================================
print("=" * 70)
print("SECTION 5: Tuples")
print("=" * 70)

# Create a tuple of colors
colors = ("red", "green", "blue")
print(f"Tuple: {colors}")

# Access elements in the tuple
print(f"First color: {colors[0]}")  # red
print(f"Second color: {colors[1]}")  # green

# Tuples are immutable - you cannot modify them
print("Attempting to modify tuple will raise an error:")
try:
    colors[0] = "yellow"
except TypeError as e:
    print(f"Error: {e}")

print(f"Tuple remains unchanged: {colors}")
print()

# =============================================================================
# SECTION 6: Dictionaries - Key-Value Pairs
# =============================================================================
print("=" * 70)
print("SECTION 6: Dictionaries")
print("=" * 70)

# Create a dictionary
alien_0 = {'color': 'green', 'points': 5}
print(f"Dictionary: {alien_0}")

# Accessing values in a dictionary
print(f"Color: {alien_0['color']}")
print(f"Points: {alien_0['points']}")

# Adding new key-value pairs
alien_0['weapon'] = 'laser'
print(f"After adding weapon: {alien_0}")

# Modifying existing values
alien_0['points'] = 10
print(f"After updating points: {alien_0}")

# Dictionary methods
print(f"Keys: {alien_0.keys()}")
print(f"Values: {alien_0.values()}")
print(f"Items: {alien_0.items()}")
print()

# =============================================================================
# SECTION 7: Sets - Unordered Collections with No Duplicates
# =============================================================================
print("=" * 70)
print("SECTION 7: Sets")
print("=" * 70)

# Creating a set from a list (removes duplicates)
num_lst = [1, 2, 2, 2, 3, 4, 5, 5]
numbers = set(num_lst)
print(f"Original list: {num_lst}")
print(f"Set (duplicates removed): {numbers}")

# Remove an element from the set
numbers.remove(3)
print(f"After removing 3: {numbers}")

# Sets automatically ignore duplicate values
numbers.add(2)  # Adding 2 again (already exists)
print(f"After adding 2 (already exists): {numbers}")

# Check if an element is in the set
print(f"Is 4 in numbers? {4 in numbers}")
print(f"Is 6 in numbers? {6 in numbers}")
print()

# =============================================================================
# SECTION 8: Set Operations
# =============================================================================
print("=" * 70)
print("SECTION 8: Set Operations")
print("=" * 70)

# Create two sets
a = set('abracadabra')
b = set('alacazam')

print(f"Set a: {a}")  # unique letters in 'abracadabra'
print(f"Set b: {b}")  # unique letters in 'alacazam'
print()

# Difference: letters in a but not in b
print(f"Difference (a - b): {a - b}")
print(f"Using .difference(): {a.difference(b)}")
print()

# Union: letters in a or b or both
print(f"Union (a | b): {a | b}")
print(f"Using .union(): {a.union(b)}")
print()

# Intersection: letters in both a and b
print(f"Intersection (a & b): {a & b}")
print(f"Using .intersection(): {a.intersection(b)}")
print()

# Symmetric Difference: letters in a or b but not both
print(f"Symmetric Difference (a ^ b): {a ^ b}")
print(f"Using .symmetric_difference(): {a.symmetric_difference(b)}")
print()

# =============================================================================
# SECTION 9: Boolean Type
# =============================================================================
print("=" * 70)
print("SECTION 9: Boolean Type")
print("=" * 70)

is_active = True
is_logged_in = False

print(f"is_active: {is_active}, type: {type(is_active)}")
print(f"is_logged_in: {is_logged_in}, type: {type(is_logged_in)}")

# Boolean operations
print(f"is_active AND is_logged_in: {is_active and is_logged_in}")
print(f"is_active OR is_logged_in: {is_active or is_logged_in}")
print(f"NOT is_active: {not is_active}")
print()

# =============================================================================
# SECTION 10: None Type
# =============================================================================
print("=" * 70)
print("SECTION 10: None Type")
print("=" * 70)

nothing = None
print(f"nothing: {nothing}, type: {type(nothing)}")

# None is often used to represent the absence of a value
result = None
if result is None:
    print("Result has not been set yet")
print()

# =============================================================================
# SECTION 11: Summary of Built-in Data Types
# =============================================================================
print("=" * 70)
print("SECTION 11: Summary of Built-in Data Types")
print("=" * 70)

print("""
Python Built-in Data Types:
- Numeric: int, float, complex
- Sequence: str, list, tuple
- Mapping: dict
- Set: set, frozenset
- Boolean: bool
- None: NoneType
- Binary: bytes, bytearray, memoryview

Key Differences:
- Lists are mutable (can be changed), Tuples are immutable (cannot be changed)
- Sets contain unique elements only, Lists can have duplicates
- Dictionaries store key-value pairs for fast lookups
- Strings are immutable sequences of characters
""")

print("=" * 70)
print("Tutorial Complete!")
print("=" * 70)
