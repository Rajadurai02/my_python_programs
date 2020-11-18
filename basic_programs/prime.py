def prime(num):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print("It is not a prime number")
                break
        else:
            print("It is a prime number")
    else:
        print("It is not a prime number")
        
prime(7)
prime(4)
prime(19)
prime(29)