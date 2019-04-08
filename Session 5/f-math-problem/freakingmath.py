from random import *

def generate_quiz():
    formula = ["+","-","*","/"]
    x = randint(0,9)
    y = randint(1,9)
    cal = choice(formula)
    if cal == "+":
        quest = x+y
    elif cal == "-":
        quest = x-y
    elif cal == "*":
        quest = x*y
    else:
        quest = x/y
    Q1 = [quest+1,quest,quest-1]
    Q2 = choice(Q1)
    # Hint: Return [x, y, op, result]
    print(x,y,cal,Q2)
    return [x,y,cal,Q2]

def check_answer(x, y, op, result, user_choice):
    pass
    
