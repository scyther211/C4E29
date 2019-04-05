price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

for key in price.keys():
    if key in stock.keys():
        print(key)
        print("Price: ",price[key])
        print("Stock left: ",stock[key])
    else:
        print("Missing item in stock list")

input("press enter to continue")
Total = 0
for key in price.keys():
    if key in stock.keys():
        money = price[key]*stock[key]
        Total += money

print("Sum of income from selling",Total)

