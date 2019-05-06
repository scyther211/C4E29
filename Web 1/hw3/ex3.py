from pymongo import MongoClient
from bson.objectid import ObjectId
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

ex_db = client.c4e

Customer_db = ex_db['customers']

a = Customer_db.count_documents({'ref':'events'})
b = Customer_db.count_documents({'ref':'ads'})
c = Customer_db.count_documents({'ref':'wom'})

print(a)

labels = ['Events', 'WoM', 'Ads']
sizes = [a,b,c]
pyplot.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
pyplot.axis('equal')
pyplot.show()