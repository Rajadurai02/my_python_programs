def big(list):
    big = 0
    for i in list:
        if i > big:
            big = i
    return big
print(big([12,4,67,84,45,32,2,4,5,34]))

