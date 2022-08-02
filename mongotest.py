import pymongo
client = pymongo.MongoClient("mongodb+srv://root:39il05@cluster0.5llae.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhamshu",
    "email":"sudhanshu@gmail.com",
    "surname":"kumar"
}
d = {
    "name":"sudhamshu",
    "email":"sudhanshu@gmail.com",
    "surname":"kumar"
}
d = {
    "name":"sudhamshu",
    "email":"sudhanshu@gmail.com",
    "surname":"kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)