import pymongo
client = pymongo.MongoClient("mongodb+srv://aditya:1999dubey@cluster0.tzczrc5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" : "aditya"  ,
    "email" : "apdubey1999@gmail.com" ,
    "surname" : "dubey"
}
db1 = client['mongo']
coll = db1['test']
coll.insert_one(d)
