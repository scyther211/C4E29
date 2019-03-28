# no = int(input("Nam sinh: "))
# ketqua = 2019 - no

# if ketqua < 10:
#     print("Child")
# elif ketqua < 18:
#     print("Teen")
# else:
#     print("Adult")

from random import *

x = randint(0,100)

if x < 30:
    print("rainy")
elif x < 70:
    print("cloudy")
else:
    print("sunny")