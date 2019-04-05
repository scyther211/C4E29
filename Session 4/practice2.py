Bangluong = []
So1 = {
    "Ten":"Hai",
    "Muc Luong": 50000,
    "Ngay lam": 25,
    "Gio/ngay": 8,
}
So2 = {
    "Ten":"Duc",
    "Muc Luong": 25000,
    "Ngay lam": 20,
    "Gio/ngay": 6,
}
So3 = {
    "Ten":"Minh",
    "Muc Luong": 20000,
    "Ngay lam": 27,
    "Gio/ngay": 5,
}
So4 = {
    "Ten":"Long",
    "Muc Luong": 10000,
    "Ngay lam": 30,
    "Gio/ngay": 3,
}
Bangluong.append(So1)
Bangluong.append(So2)
Bangluong.append(So3)
Bangluong.append(So4)
# Ten_nv = input("Nhap ten nhan vien muon tra cuu: ")
# for person in Bangluong:
#     if Ten_nv == person["Ten"]:
#         Luongthang = person["Muc Luong"]*person["Ngay lam"]*person["Gio/ngay"]
#         print(Luongthang)
#         break

Total_salary = 0
for person in Bangluong:
    Luong = person["Muc Luong"]*person["Ngay lam"]*person["Gio/ngay"]
    Total_salary = Total_salary + Luong
print(Total_salary)

    
    
    


