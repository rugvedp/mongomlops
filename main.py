import pymongo
client = pymongo.MongoClient("mongodb+srv://capsule:12345@capsule.fzj2u.mongodb.net/Imp")

database = client["Imp"]
collection = database['Tees']
all = collection.find()

for idx, val in enumerate(all):
    print(val['name'])