try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("You can't divide by zero!")
