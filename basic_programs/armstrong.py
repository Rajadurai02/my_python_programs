def arm(num):
    org = num
    arm = 0
    while num > 0:
        
        a = num % 10
        arm = arm + a**3
        num = num // 10
    if org == arm:
        print("this is armstrong number")
    else:
        print("this is not a armstrong number")
arm(153)