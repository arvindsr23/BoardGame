import person
import dice
import pymongo
from pymongo import MongoClient
from collections import namedtuple

client = MongoClient()
db = client.boardGame
#db.playerName.insert_one({"Name":"Hello World"})
#client.close()

class main:

    def isBlank(s):
        if (s and s.strip()):
            return False
        else:
            return True

    plyrList = []
    numpl = int(input("How many Players ?"))
    num = person.player.numPlayer(numpl)

    player = namedtuple('player','name wins')
    doc = {}

    i=0
    for d in db.playerName.find():
        doc[i] = player(name=d['name'], wins=d['wins'])
        i=i+1
    print(doc)




    for i in range(0, num):
        playerNames = input("Enter each person's name:")
        if isBlank(playerNames) is True:
            print("Enter a proper Name")
        else:
            plyr = person.player(playerNames,0,0)
            #db.playerName.insert_one({"name":plyr.name})
            #client.close()
            plyrList.append(plyr)


    for k in doc:
        for l in range(0,num):
            if doc[k].name == plyrList[l].name:
                plyrList[l].count = doc[k].wins


    for i in range(0,num):
        print("Name: %s" % plyrList[i].name, "Score: %d" % plyrList[i].score, "Count: %d" % plyrList[i].count)
        if plyrList[i].count==0:
            db.playerName.insert_one({"name":plyrList[i].name,"wins":plyrList[i].count})

    plyrList[0].score = 95
    plIndex=0
    while (plyrList[plIndex].score < 100):
        print("*-------- Run Number: %d" % plyrList[plIndex].count, "-----*")
        indScore = dice.dice.dice(0)
        plyrList[plIndex].score = plyrList[plIndex].score + indScore
        if plyrList[plIndex].score >= 100:
            db.playerName.find_one_and_update({"name": plyrList[plIndex].name}, {"$inc": {"wins": 1}})
            #for doc in db.playerName.find({"name":plyrList[plIndex].name}):
             #   print(plyrList[plIndex].name,"wins! with a score of",plyrList[plIndex].score,".",plyrList[plIndex].name,"has won", doc['wins'], "games")
            print(plyrList[plIndex].name, "wins! with a score of", plyrList[plIndex].score, ".", plyrList[plIndex].name,"has won", plyrList[plIndex].count , "games")
            client.close()
            break
        print("Name: %s" % plyrList[plIndex].name, "Score: %d" % plyrList[plIndex].score)
        print ("plIndex %d" % plIndex, "num %d" % num)
        if plIndex == num-1:
            plIndex = 0
        else:
            plIndex += 1
        plyrList[plIndex].count += 1
        diceReady = input(plyrList[plIndex].name)










    #for i in range(0, len(playerNames)):
    #    namesp = person.player.personNames("", playerNames)
    #valDice = dice.dice.dice()
    #print(num)
    #print(namesp)
    #print(valDice)
