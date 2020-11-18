class Marathon:
    def marathon():
        distance = 120
        print("enter distance covered by participents in marathon and press q to terminate:")
        dist_list = []
        while True:
            dist = input()
            if dist == 'q':
                break
            else:
                dist_list.append(dist)
        print(dist_list)
        less = []
        com = []
        for i in dist_list:
            if float(i) > 0:
                if float(i) < distance:
                    less.append(float(i))
                else:
                    com.append(float(i))
            else:
                print("invalid input")
                break
        print("less covered participents")
        print(less)
    marathon()
marathon1 = Marathon()
