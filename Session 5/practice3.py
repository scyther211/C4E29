from random import *
from functions.calculate import calculate
i = 0
quest = 0
formula = ["+","-","*","/"]
loop = True
while loop:
    x = randint(0,9)
    y = randint(1,9)
    cal = choice(formula)
    calculate(x,y,cal)
    # error = choice([-1,0,0,0,0,1]) -> add more 0 to increase rate of true answer
    # display_answer = quest + error
    Q1 = [quest+1,quest,quest-1]
    Q2 = choice(Q1)
    print("{0} {1} {2} = {3}".format(x,*cal,y,Q2))
    answer = input("Y/N ? ").upper()
    if answer == "Y" and Q2 == quest:
        print("correct")
        i += 1
    elif answer == "Y" and Q2 != quest:
        print("wrong")
        loop = False
        print("Your score: ",i)
    elif answer == "N" and Q2 == quest:
        print("wrong")
        loop = False
        print("Your score: ",i)
    elif answer == "N" and Q2 != quest:
        print("correct")
        i += 1
    else:
        print("wrong answer input")
        loop = False
        




