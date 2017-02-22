class player:

    name = []
    score = 0
    count = 0
    def __init__(self,nm,sc,ct):
        self.name = nm
        self.score = sc
        self.count = ct




    def numPlayer(num):
        if num<2:
            return "Need 1 more player"
        else:
            return num

    def personNames(self, nm):
        if nm in (""):
            return "Fill Name"
        else:
            return nm







