# This is an example of raising and handling an exception.

try:
    number = 10
    if number > 5:
        raise ValueError(f"The number should not exceed 5. ({number=})")
    print(number)
except ValueError as e:
    print("Caught an exception:", e)
else:
    print("No exceptions were raised. The number is valid.")
