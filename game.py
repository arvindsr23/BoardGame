import person
import dice

class main:

    def isBlank(s):
        if (s and s.strip()):
            return False
        else:
            return True

    def initPrint(plyrObj):

        print(plyrObj.name)
        print(plyrObj.score)
        print(plyrObj.count)


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
        indScore = dice.dice.dice(0)
        plyrList[plIndex].score = plyrList[plIndex].score + indScore
        print("Name: %s" % plyrList[plIndex].name, "Score: %d" % plyrList[plIndex].score)
        print ("plIndex %d" % plIndex, "num %d" % num)
        if plIndex == num-1:
            plIndex = 0
        else:
            plIndex += 1










    #for i in range(0, len(playerNames)):
    #    namesp = person.player.personNames("", playerNames)
    #valDice = dice.dice.dice()
    #print(num)
    #print(namesp)
    #print(valDice)
