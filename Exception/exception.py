try:
    x=float(input("enter a number:"))
    y=float(input("enter another number:"))
    result=str(x/y)
    print(result)
except ZeroDivisionError:
    print("divide by zero error")
    raise
finally:
    print("this code run what ever the error will occur")
