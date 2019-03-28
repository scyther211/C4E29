user = input("User name: ")
p = input("Password: ")

if user == "c4e"  and p == "codethechange":
    print("Welcome to hell")
elif user == "c4e"  and p != "codethechange":
    print("wrong password")
elif user != "c4e" and p == "codethechange":
    print("wrong ID")
else:
    print("wrong ID or password")