num_1 = 0
num_2 = 0
sw1 = 1
while sw1 == 1:
    print(" welcome this is totally a normal calculator\n lol ")
    print(" pick an option öwö")
    print(" 1.- add")
    print(" 2.- sub")
    print(" 3.- multiply")
    print(" 4.- Divide")
    print(" 0.- exit")
    op = int(input(" so = ? ...  "))
    if op == 1:
        num_1 = int(input(""))
        print(" So u have choosen death ...\n just kidding,.., lol\n+")
        print(" u choosen addition ")
        num_2 = int(input(""))
        num_3 = num_1 + num_2
        print(" the answer iss ...")
        print(f"{num_1} + {num_2} = {num_3}")
    if op ==2:
        print(" come on, this one its hard\n -")
        num_1 = int(input(""))
        num_2 = int(input(""))
        num_3 = num_1 - num_2
        print(" the answer iss ...")
        print(f"{num_1} - {num_2} = {num_3}")
    if op ==3:
        print(" I love this one, its like 1.- but many many times!\n*")
        num_1 = int(input(""))
        num_2 = int(input(""))
        num_3 = num_1 * num_2
        print(" the answer iss ...")
        print(f"{num_1} * {num_2} = {num_3}")
    if op ==4:
        print(" oke I might have a lil trick under the sleeve lol\n/")
        num_1 = int(input(""))
        num_2 = int(input(""))
        while num_2 == 0:
            num_2 =int(input(""))
        num_3 = num_1 / num_2
        print(" the answer iss ...")
        print(f"{num_1} / {num_2} = {num_3}")
    if op ==0:
        sw1 = 0