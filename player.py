class Player():
    def __init__(self, app):
        self.money = 0
        self.currentDay = 1
        
    def playGame(self, app):
        app.day = Day(self.currentDay)
        