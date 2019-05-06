from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

Base = client.c4e

River_db = Base["river"]

# Africa_rivers = River_db.find({'continent':'Africa'})
# for river in Africa_rivers:
#     print(river["name"])

American_rivers = River_db.find({'$and':[
    {'continent':'S.America'},
    {'length':{'$lt':1000}}
]})
for river in American_rivers:
    print(river['name'])