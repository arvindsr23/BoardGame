import person
import dice
import pymongo

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client.boardGame


class main:

    def isBlank(s):
        if (s and s.strip()):
            return False
        else:
            return True

    plyrList = []
    numpl = int(input("How many Players ?"))
    num = person.player.numPlayer(numpl)

    for i in range(0, num):
        playerNames = input("Enter each person's name:")
        if isBlank(playerNames) is True:
            print("Enter a proper Name")
        else:
            plyr = person.player(playerNames,0,0)
            plyrList.append(plyr)

    for i in range(0,num):
        print("Name: %s" % plyrList[i].name, "Score: %d" % plyrList[i].score, "Count: %d" % plyrList[i].count)

    plIndex=0
    while (plyrList[plIndex].score < 100):
        print("*-------- Run Number: %d" % plyrList[plIndex].count, "-----*")
        indScore = dice.dice.dice(0)
        plyrList[plIndex].score = plyrList[plIndex].score + indScore
        if plyrList[plIndex].score >= 100:
            print(plyrList[plIndex].name,"wins! with a score of",plyrList[plIndex].score)
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
