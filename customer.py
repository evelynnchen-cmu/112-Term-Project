import random

class Customer():
    
    def __init__(self, app):
        self.order = []
        self.makeRandomOrder(app)
        self.waitTime = 0
        
    def makeRandomOrder(self, app):
        randomInt = random.randint(0, len(app.inventory.teaOPTIONS)-1)
        self.order.append(app.inventory.teaOPTIONS[randomInt])
        randomInt = random.randint(0, len(app.inventory.toppingsOPTIONS)-1)
        self.order.append(app.inventory.toppingsOPTIONS[randomInt])
        randomInt = random.randint(0, len(app.inventory.sugarOPTIONS)-1)
        self.order.append(app.inventory.sugarOPTIONS[randomInt])
        randomInt = random.randint(0, len(app.inventory.iceOPTIONS)-1)
        self.order.append(app.inventory.iceOPTIONS[randomInt])
        randomInt = random.randint(0, len(app.inventory.milkOPTIONS)-1)
        self.order.append(app.inventory.milkOPTIONS[randomInt])
        