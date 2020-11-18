import multiprocessing
def square(num):
    square = num ** 2
    print("Square is : {}".format(square))
def cube(num):
    cube = num ** 3
    print("Cube is : {}".format(cube))
if __name__ == "__main__":
    p1 = multiprocessing.Process(target = square,args = (10,))
    p2 = multiprocessing.Process(target = cube,args = (10,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("done")