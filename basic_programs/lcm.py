def lcm(num1,num2):
    if num1 > num2:
        great = num1
    else:
        great = num2
    while(True):
        if (great % num1 == 0) and (great % num2 == 0):
            lcm = great
            break
        great += 1
    return great
print(lcm(23,56))