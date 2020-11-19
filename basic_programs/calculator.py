def calculator():
    while True:
        print("enter + for addition")
        print("enter - for subtraction")
        print("enter * for multiplication")
        print("enter / for division")
        print("enter quit for existing the application")
        
        text=input(":")

        if text=="+":
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
            result=str(num1+num2)
            print("the result is:"+result)
        elif text=="-":
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
            result=str(num1-num2)
            print("the result is:"+result)
        elif text=="*":
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
            result=str(num1*num2)
            print("the result is:"+result)
        elif text=="/":
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
            result=str(num1/num2)
            print("the result is:"+result)
        elif text=="quit":
            break
        else:
            print("invalid input")
calculator()

