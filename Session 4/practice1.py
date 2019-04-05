tudienso = {
    "ONE": "Mot",
    "TWO": "Hai",
    "THREE": "Ba",
}

print("welcome to number converter, we currently can translate (press quit to turn off): ")
print(" * "*10)
loop = True
while loop:
    for key in tudienso.keys():
        print(key,end=' ')
    print()
    N = input("Type your number to translate: ").upper()
    if N in tudienso.keys():
        print(tudienso.get(N))
        print(" * "*10)
    elif N == "QUIT":
        loop = False
        print("Thank you for using!")
    else:
        M = input("Do you want to add new definition ? (Y/N): ").upper()
        if M == "N":
            print("Thank you and goodbye")
            print(" * "*10)
        elif M == "Y":
            E = input("Input new definition: ")
            tudienso[N]=E
            print("Thank you")
            print(" * "*10)
        else:
            print("Please input correct value")
            print(" * "*10)