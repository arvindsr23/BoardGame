import pymongo
import bson

import pprint
from collections import namedtuple

from pymongo import MongoClient

client = MongoClient()
db = client.boardGame

player = namedtuple('player', 'name wins')
doc = {}

i=0
for d in db.playerName.find():
        doc[i] = player(name=d['name'], wins = d['wins'])
        i=i+1


for key,value in sorted(doc.items()):
    print (key,value)

print (doc[0].name)




#self.request.db.playerName.find().forEach(bson.Code('''function (myDoc) {(myDoc.wins)}'''))


#for u in self.request.db.playerName.find():
#    self.request.db.playerName.find_one({}, {'_id': 0})


#pprint.pprint(db.playerName.find_one({"name":"Earth"},{"_id":0,"wins":1}))

#arr = list(db.playerName.find_one({"name":"Earth"},{"_id":0,"wins":1}))
#print(arr [0])



#for doc in db.playerName.find({"name":"Earth"}):    print(doc['wins'])




#print(db.playerName.count())

client.close()


