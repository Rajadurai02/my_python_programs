def rev_num(num):
    rev = 0
    while num > 0:
        a = num % 10
        rev = rev * 10 + a
        num = num // 10
    return rev
print(rev_num(54245786))
