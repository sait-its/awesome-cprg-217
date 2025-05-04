# This is an example of raising an exception.

number = 10
if number > 5:
    raise Exception(
        f"The number should not exceed 5. ({number=})")
print(number)
