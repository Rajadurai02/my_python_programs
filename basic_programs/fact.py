def fact(num):
    if num > 0:
        fact = 1
        for i in range(1,num+1):
            fact = fact * i
    else:
        print("enter corrcet number")
    return fact
print(fact(1))