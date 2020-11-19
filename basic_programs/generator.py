def countdown():
    i=10
    while i>0:
        yield i
        i-=1
for i in countdown():
    print(i)



def makeword():
    word=""
    for ch in "raja":
        word+=ch
        yield word

print(list(makeword()))
