from flask import Flask, render_template,request
from pymongo import MongoClient

app = Flask(__name__)

uri = 'mongodb+srv://admin:admin@c4e29-cluster-qtb0x.mongodb.net/test?retryWrites=true'

client = MongoClient(uri)
first_db = client.first_db
bike_collection = first_db['bike_collection']

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
        bike_collection.insert_one(new_bike)
        print(new_bike)
        return "Thank you for submitting"

if __name__ == '__main__':
  app.run(debug=True)
 