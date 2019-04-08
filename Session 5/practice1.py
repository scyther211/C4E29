x = int(input("x = "))
y = int(input("y = "))
cal = input("formular (+,-,*,/) = ")
result = 0
# if cal == "+":
#     print("result =",x+y)
# elif cal == "-":
#     print("result =",x-y)
# elif cal == "*":
#     print("result =",x*y)
# elif cal == "/":
#     print("result =",x/y)
# else:
#     print("please insert correct symbol")

# REFACTOR
if cal == "+":
    result = x+y
elif cal == "-":
    result = x-y
elif cal == "*":
    result = x*y
elif cal == "/":
    result = x/y
else:
    print("please insert correct symbol")
print("{0} {1} {2} = {3}".format(x,cal,y,result))