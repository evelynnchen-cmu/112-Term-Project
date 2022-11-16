#classes
from cmu_112_graphics import *
import random

class Day():
    def __init__(self, neededAccuracy):
        self.dayTime = 5 #should be 120
        self.neededAccuracy = neededAccuracy
        print(self.neededAccuracy)
        
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

#functions
def checkIfDayOver(app):
    # if app.currentDayIndex > 7:
    #     app.mode = 'gameOverScreen'
    if app.currentDay.dayTime == 0:
        app.mode = 'dayOverScreen'
    else:
        app.currentDay.dayTime -= 1
        print(app.currentDay.dayTime)

def checkIfGameOver(app):
    #check lose condition too
    if app.currentDayIndex > 7:
        app.mode = 'gameOverScreen'

def startNewDay(app):
    if app.money < 0:
        app.difficulty = 'baby'
    app.currentDay = Day(app.difficulty)
    app.currentDayIndex += 1
   
#helpers

def drawButton(canvas, dimensionTuple, buttonName):
    x0, y0, x1, y1 = dimensionTuple
    buttonWidth = abs(x0-x1)
    buttonHeight = abs(y0-y1)
    canvas.create_rectangle(x0, y0, x1, y1, fill = 'lightblue1', width = 3)
    canvas.create_text(x0 + (buttonWidth/2), y0 + (buttonHeight/2), text = buttonName, 
                            font = 'Arial 15 bold', fill = 'black')

def isValidClick(x, y, dimensionTuple):
    x0, y0, x1, y1 = dimensionTuple
    if (x0 < x < x1) and (y0 < y < y1):
        return True
    return False

# copied from TA Mini-Lecture: Advanced Tkinter Mini Lecture
def scaleImage(app, image, box):
    
    originalWidth, originalHeight = image.size
    originalRatio = originalWidth/originalHeight
    width, height = box
    goalRatio = width/height
    
    if originalRatio > goalRatio:
        scale = width/originalWidth
    else:
        scale = height/originalHeight
    
    return app.scaleImage(image, scale)
    