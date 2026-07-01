a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))

if b == 0:
    raise ZeroDivisionError("Our program is not meant to divide a number by zero")
else:
    print(f"The division a/b is {a / b}")