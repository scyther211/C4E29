from random import *
db = ["spartan","samurai","templar","winged"]
print("""
Welcome to Word Jumble!

Find the hidden words by matching the letters""")

input("press enter button to start ")
loop = True
answer = choice(db)
while loop:
    J1 = list(answer)
    J2 = sample(J1,len(J1))
    print("Here is your letter: ",end='')
    print(*J2,sep=" ,")
    rep = input("Type your answer: ")
    if rep == answer:
        print("Correct")
        loop = False
    else:
        print("Not correct, please try again")

    
    