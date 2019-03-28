wkg = int(input("Can nang (kg): "))
hcm = int(input("Chieu cao (cm): "))

hcm1 = hcm*0.01

BMI = wkg/(hcm1*hcm1)

if BMI < 16:
    print("Thieu can")
elif BMI < 18.5:
    print("Hoi thieu can")
elif BMI < 25:
    print("Binh thuong")
elif BMI <30:
    print("Hoi thua can")
else:
    print("Thua can")