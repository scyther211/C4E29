a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("vo nghiem")    
elif delta == 0:
    print("Co 1 nghiem: ")
    x = -b/2*a
    print(x)
else:
    print("Co 2 nghiem: ")

    x1 = (-b + delta**0.5)/2*a
    x2 = (-b - delta**0.5)/2*a
    print("nghiem 1:",x1," nghiem 2: ",x2)