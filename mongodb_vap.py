import requests # gets the data from API
from pymongo import MongoClient
import json
client = MongoClient('localhost:27017')

db = client.UserEntity # create local UserEntity database on the fly

def entity_insert(data=None):

    print(data)
    db.entity.insert(data)
    return "Entity registered"

def entity_get():
    cur = db.entity.find({}, {"_id": 0})
    cur_list = []
    for i in cur:
        # print(i)
        cur_list.append(i)
    res = json.dumps(cur_list)
    return res