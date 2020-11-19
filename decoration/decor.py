def decor(func):
    def wrap():
        print("====================")
        func()
        print("====================")
    return wrap

def print_text():
    print("I AM RAJADURAI!")
print_text=decor(print_text)
print(print_text)
