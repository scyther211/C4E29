shop = ["T-Shirt", "Sweater"]
loop = True
while loop:
    answer = str(input("Welcome to our shop, what do you want (C, R, U, D)? "))
    if answer == "R":
        print("Our items: ",end='')
        print(*shop,sep=' ,')
        loop = False
    elif answer == "C":
        new = str(input("Enter new item: "))
        shop.append(new)
        print("Our items: ",end='')
        print(*shop,sep=' ,')
        loop = False
    elif answer == "U":
        position = int(input("Update position? "))
        if position < 0:
            position = int(input("Please update different position? "))
        elif position > len(shop):
            position = int(input("Please update different position? "))
        item = str(input("New item? "))
        shop.insert(position-1,item)
        print("Our items: ",end='')
        print(*shop,sep=' ,')
        loop = False
    elif answer == "D":
        D = int(input("Delete position? "))
        del shop[D-1]
        print("Our items: ",end='')
        print(*shop,sep=' ,')
        loop = False
    else:
        print("Please insert correct symbol")
        answer = str(input("Welcome to our shop, what do you want (C, R, U, D)? "))

