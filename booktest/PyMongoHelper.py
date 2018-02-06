# -*- coding:utf-8 -*-
from pymongo import *

# uri 形式 mongodb://admin:123@127.0.0.1:27017/test
client = MongoClient(host="127.0.0.1", port=27017)
db = client.test
t1 = db.t1
# db.t1.insert({"date": "20180129"})

# new_id = db.t1.insert_one({"adwdaw": "dawdaw"}).inserted_id

# db.t1.update_one({"date": "20180129"}, {"$set": {"date": "20180130"}})

# t1.delete_one({"name":"pxd"})
# for item in db.t3.find():
#     for x in item.items():
#         print(x[1])

cursor = t1.find({'age': {'$gt': 20}}).sort('age',DESCENDING)
cursor = t1.find({'age': {'$gt': 20}}).sort([('age',DESCENDING),('age',DESCENDING)])
cursor = t1.find({'age': {'$gt': 20}}).skip(2).limit(2)
for x in cursor:
    print(x["age"])







# print(new_id)
