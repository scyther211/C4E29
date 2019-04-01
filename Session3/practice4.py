print('''
Nghi 1 so tu 1 den 100, Toi se doan so cua ban
Nhap "l" neu so lon hon, Nhap "n" neu nho hon, Nhap "d" neu dung''')
loop = True
i1 = 0
i2 = 100
while loop:
    i = (i1+i2)//2
    # n = input(str(i) + " co dung ko: ")
    n = input("{} co dung ko: ".format(i))
    if n == "d":
        loop = False
        print("doan dung roi")
    elif n == "l":
        i1 = i
    elif n == "n":
        i2 = i
    else:
        print("Chi nhap n hoac l hoac d thoi")
