def sum_of_digit(num1):
    sum = 0
    for i in str(num1):
        sum += int(i)
    return sum
print(sum_of_digit(7773))