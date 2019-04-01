n=int(input("Nhap so:"))
loop = True
m = 2
while loop:
    if n%m == 0:
        loop = False
        print("Khong phai")
    m += 1
    if m == n:
        loop = False
        print("SNT")


# Cach 2

# n=int(input("Enter number:"))
# is_prime = True
# i = 2
# while i*i<n:
#     if n % i == 0:
#         is_prime = False
#     i += 1       
#     if is_prime:
#         print("SNT")
#     else:
#         print("Ko phai")


