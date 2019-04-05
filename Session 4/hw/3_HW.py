question = {
    "1 + 1 = ?": [2,3,10,15],
    "2 x 2 = ?": [4,9,16,22],
    "4 + 1 = ?": [5,6,7,8],
}
answer = [2,4,5]

from random import *
Ask = choice(list(question))
print("The game is on you dumbass, answer the following question")
print(Ask)
print(" * "*10)
i = 0
rep = sample(question[Ask],len(question[Ask]))
for i in range(4):
    print(i+1,". ",rep[i])
    i += 1
loop = True
while loop:
    ans = int(input("Please input your answer: "))
    if ans in rep:
        if ans in answer:           
            print("correct")
            loop = False
        else:
            print("Not correct")
            loop = False
    else:
        print("Please type one of given choice")

