from flask import Flask, render_template,request
app = Flask(__name__)

bike = []

@app.route('/new_bike',methods=["GET","POST"])
def index():
    if request.method == 'GET':        
        return render_template('rent_bike.html')
    if request.method == 'POST':
        bike_form = request.form
        new_bike = {
            "Bike_Model" : bike_form['Model'],
            "Daily_fee" : bike_form['Daily_fee'],
            "Image_Link" : bike_form['Image'],
            "Year" : bike_form['Year'],
        }
        bike.append(new_bike)
        print(new_bike)
        return "Thank you for submitting"

if __name__ == '__main__':
  app.run(debug=True)
 