#classes
import random

class Day():
    def __init__(self, neededAccuracy):
        self.dayTime = 120
        self.neededAccuracy = neededAccuracy
        
        

class Customer():
    def __init__(self, app):
        self.order = []
        self.makeRandomOrder(app)
        self.waitTime = 0
        
    def makeRandomOrder(self, app):
        self.order.append(random.randomchoice(app.teaOPTIONS))
        self.order.append(random.randomchoice(app.teaOPTIONS))
        self.order.append(random.randomchoice(app.toppingsOPTIONS))
        self.order.append(random.randomchoice(app.sugarOPTIONS))
        self.order.append(random.randomchoice(app.iceOPTIONS))
        self.order.append(random.randomchoice(app.milkOPTIONS))
    