from pymongo import MongoClient
from bson.objectid import ObjectId

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

ex_db = client.c4e

Post_data = ex_db["posts"]

new_post = {
    "title" : "One last thing",
    "author" : "Minh Le",
    "content" : "Shit happens and life goes on"
}

Post_data.insert_one(new_post)