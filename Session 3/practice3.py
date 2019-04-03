import random

x = random.randint(0,100)

loop = True
while loop:
    n = int(input("Chon 1 so tu 0-100: "))
    if n == x:
        loop = False
        print("doan dung roi")
    elif n < x:
        print("Lon Hon")
    elif n > x:
        print("Nho hon")
