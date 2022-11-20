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
        for i in range(5):
            self.order.append(random.randomchoice(app.OPTIONS[i]))

###################################
#functions
###################################
#entire game
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
        app.neededAccuracy = 60
    app.currentDay = Day(app.dayLength, app.neededAccuracy)
    app.dayIndex += 1

#shop and store
def drawDayProgBar(app, canvas):
    
    canvas.create_rectangle(15, 10, 502, 50, width=3)
    daySlice = (485/app.dayLength)*(app.dayLength-app.currentDay.dayTime)
    canvas.create_rectangle(17, 12, 17+daySlice, 49, width=0, fill='chartreuse4')
    canvas.create_text(257.5, 30, text=f'Day {app.dayIndex}', font='Arial 15 bold')

#kitchen
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

#called in kitchen --> evaluation
def evaluateDrink(app):
    correctIngs = 0
    miscalIngs = 0
    wrongIngs = 0
    missingIngs = 0
    #order: toppings sugar ice milk tea
    
    #build up correctDrinkDict
    for i in range(len(app.curCustDrink)-1):
        app.correctDrinkDict[app.curCustDrink[i]] = app.times[i][app.curCustDrink[i]]
    
    #get tea's (last elem) correct time based on previous ings
    teaTime = 0
    otherTimes = 0
    for ing in app.correctDrinkDict:
        
        otherTimes += app.correctDrinkDict[ing]
        teaTime = 20 - otherTimes
    app.correctDrinkDict[app.curCustDrink[-1]] = teaTime
    
    for ing in app.correctDrinkDict:
        if ing in app.madeDrinkDict:
            print(f'yes, {ing} in {app.madeDrinkDict}')
            madeIngTime = app.madeDrinkDict[ing]
            correctIngTime = app.correctDrinkDict[ing]
            errorMargin = 1-(app.currentDay.neededAccuracy/100)
            lowEnd = (1-errorMargin)*correctIngTime
            highEnd = (1+errorMargin)*correctIngTime
            
            if lowEnd < madeIngTime < highEnd:
                correctIngs += 1
            else:
                miscalIngs += 1
        else:
            print(f'no, {ing} not in {app.madeDrinkDict}')
            missingIngs += 1
            
    for ing in app.madeDrinkDict:
        if ing not in app.correctDrinkDict:
            wrongIngs += 1
    #correct ings - 70%
    #wait time - 20%
    #miscalculations, missing, wrong - 10%
    app.drinkAccuracy = correctIngs
    print(f'correct: {correctIngs}, miscalculated: {miscalIngs}, missing: {missingIngs}, wrong: {wrongIngs}')
    print(app.drinkAccuracy)
        
    # print(app.currentDay.neededAccuracy)

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
    