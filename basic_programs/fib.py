def fibo():
    terms = int(input("Enter how many sequence?:"))
    n1 = 0
    n2 = 1
    count = 0
    if terms <= 0:
        print("please enter a positive number")
    elif terms == 1:
        print(n1)
    else:
        print("fibanocci series starts:\n")
        while count < terms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
fibo()
