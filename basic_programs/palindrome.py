#check number is palindrome
def num_palin(number):
    org = number
    palin = 0
    while number > 0:
        a = number % 10
        palin = palin * 10 + a
        number = number // 10
    if (org == palin):
        print("This number  is a palindrome")
    else:
        print("This number  is not a palindrome")
num_palin(454)
num_palin(456)

#check string is a palindrome
def str_palin(str):
    palin = str[::-1]
    if str == palin:
        print("This string is palindrome")
    else:
        print("This is not a palindrome")
str_palin("hello")
str_palin("mam")
