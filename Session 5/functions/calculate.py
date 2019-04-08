def calculate(x,y,cal):
    if cal == "+":
        quest = x+y
    elif cal == "-":
        quest = x-y
    elif cal == "*":
        quest = x*y
    else:
        quest = x/y
    return quest