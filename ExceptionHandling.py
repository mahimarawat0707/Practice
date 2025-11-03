try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("That's not a number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
