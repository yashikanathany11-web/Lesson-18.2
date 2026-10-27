try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    result = n1/n2
    print("Result is", result)
except ZeroDivisionError:
    print("Division by zero is error !!")
except ValueError:
    print("Please enter valid whole numbers")
except:
    print("Wrong input")
else:
    print("No exception.")
finally:
    print("This will execute no matter what..")