from flask import Flask, render_template,request,redirect
app = Flask(__name__)
foods = [
    {
        "title" : "Big Mac",
        "description" : "Fat and unhealthy",
        "Link": "https://assets3.thrillist.com/v1/image/2797371/size/tmg-article_default_mobile.jpg",
        "Type":"Eat"
    },
    {
        "title" : "Taco",
        "description" : "Tasty and spicy",
        "Link": "https://www.tacobell.com/images/22101_crunchy_taco_supreme_269x269.jpg",
        "Type":"Eat"
    },
    {
        "title" : "Bun Cha",
        "description" : "Godly taste",
        "Link": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1O-y3zOwEikFVDJdIOEI6VNSxtPr3R3nWDn2Csp_Wimc8fFjS",
        "Type":"Eat"
    },
    {
        "title" : "Rum",
        "description" : "Strong and dry",
        "Link": "https://www.haskells.com/media/catalog/product/cache/1/image/816x1200/040ec09b1e35df139433887a97daa66f/1/4/140324_0_1_1.jpg",
        "Type":"Drink"
    },
    {
        "title" : "Coconut",
        "description" : "tasty",
        "Link": "https://media.mercola.com/assets/images/foodfacts/coconut-water.jpg",
        "Type":"Drink"
    },
    {
        "title" : "Water",
        "description" : "Basic dehydration",
        "Link": "https://i.dawn.com/primary/2018/10/5bcbe259cef7c.jpg",
        "Type":"Drink"
    },
    ]


@app.route('/')
def index():
    return "Type /Add"

@app.route('/Add/<int:x>/<int:y>')
def Add(x,y):
    return str(x + y)

@app.route('/food')
def food():
    return render_template('food.html',foods = foods)

@app.route('/food/<int:index>')
def detail(index):
    food_details = foods[index]
    return render_template('food_detail.html', food_details = food_details)

@app.route('/food/add_food', methods=['GET','POST'])
def add_food():
    if request.method == 'GET':
        return render_template('add_food.html')
    elif request.method == 'POST':
        form = request.form
        new_food = {
            "title" : form['Title'],
            "description" : form['Description'],
            "Link": form['Link'],
            "Type":form['Type']
        }
        foods.append(new_food)
        return redirect('/food', code=302)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form = request.form
        ID = form['ID']
        password = form['password']
        if ID =='C4E' and password == '12345678':
            return "Welcome to C4E"
        else:
            return "Wrong ID or password"

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        form = request.form
        print(form)
        return "Registration fail"
        
if __name__ == '__main__':
  app.run(debug=True)