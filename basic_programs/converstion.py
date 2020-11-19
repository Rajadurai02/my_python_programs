def con_dec(num):
    print(bin(num),"in binary")
    print(oct(num),"in octal")
    print(hex(num),"in hexadecimal")
con_dec(9)

def BinaryToDecimal(binary): 
    decimal = 0 
    for digit in str(binary): 
        decimal = decimal*2 + int(digit) 
    print("The decimal value is:", decimal)
BinaryToDecimal(1110)