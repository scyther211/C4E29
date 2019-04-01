m = ["do","doo","doooo"]
print("we already have ")
for index,item in enumerate(m):
    print(index+1, item, sep='. ')
n = input("Add one more: ")
m.append(n)
for index,item in enumerate(m):
    print("{}. {}".format(index+1, item))