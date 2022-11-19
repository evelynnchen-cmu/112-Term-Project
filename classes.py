from cmu_112_graphics import *
import random
import time

###################################
#classes
###################################
class Day():
    def __init__(self, dayLength, neededAccuracy):
        self.dayTime = dayLength
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

###################################
#functions
###################################
def checkIfDayOver(app):
    if app.currentDay.dayTime == 0:
        app.mode = 'dayOverScreen'
    else:
        app.currentDay.dayTime -= 1
        # print(app.currentDay.dayTime)

def checkIfGameOver(app):
    #check lose condition too
    if app.dayIndex > 7:
        app.mode = 'gameOverScreen'

def startNewDay(app):
    if app.money < 0:
        app.difficulty = 'baby'
    app.currentDay = Day(app.dayLength, app.difficulty)
    app.dayIndex += 1
    
def drawDayProgBar(app, canvas):
    
    canvas.create_rectangle(15, 10, 502, 50, width=3)
    daySlice = (485/app.dayLength)*(app.dayLength-app.currentDay.dayTime)
    canvas.create_rectangle(17, 12, 17+daySlice, 49, width=0, fill='chartreuse4')
    canvas.create_text(257.5, 30, text=f'Day {app.dayIndex}', font='Arial 15 bold')

def getIngColor(app, ing):
    if ing == 'tapioca':
        return 'tan4'
    elif ing == 'aloe_jelly':
        return 'lemonchiffon'
    elif ing == 'red_bean':
        return 'orangered4'
    elif ing == 'pudding':
        return 'khaki'
    elif ing in app.teaOPTIONS:
        return 'bisque3'
    elif ing in app.iceOPTIONS:
        return 'slategray1'
    elif ing in app.milkOPTIONS:
        return 'mintcream'
    elif ing in app.sugarOPTIONS:
        return 'palegoldenrod'

###################################   
#helpers
###################################
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
    