#using for loop
def rev_for(string):
    str = ''
    for i in string:
        str = i + str
    return str
print(rev_for("hello world"))


#using recursion
def rev_rec(string):
    if len(string) == 0:
        return string
    else:
        return rev_rec(string[1:]) + string[0]
print(rev_rec("hi! hello"))


#using slice
def rev_slice(string):
    rev = string[::-1]
    return rev
print(rev_slice("rajadurai"))

#using reversed
def rev_rev(s):
    str =''.join(reversed(s))
    return str
print(rev_rev("haool"))
