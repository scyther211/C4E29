from random import *

sheep1 = []
for i in range(7):
    sheep1.append(randint(1,200))
print("List of sheeps: ",sheep1)
input("press enter button to continue to 2.2 and 2.3: ")
n = max(sheep1)
m = sheep1.index(n)
print("The biggest sheep's size is ",n," and let shear it")
sheep1[m] = 8
print("List of sheeps now: ",sheep1)
input("press enter button to continue to 2.4 and 2.5: ")
month = int(input("Type the number of months you want to: "))
vari = 1
while vari <= month:
    for i in range(len(sheep1)):
        sheep1[i] += 50
    print("List of sheeps after ",vari," month is ",sheep1)
    n1 = max(sheep1)
    m1 = sheep1.index(n1)
    print("The biggest sheep's size of month ",vari," is ",n1," and let shear it")
    sheep1[m1] = 8
    print("List of sheeps after: ",sheep1)
    vari += 1
input("press enter button to continue to 2.6: ")
total = sum(sheep1)
print("My flock has size in total: ",total)
print("I would get ",total," x2$", " = ",total*2,"$")


