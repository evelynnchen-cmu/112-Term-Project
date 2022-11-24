from cmu_112_graphics import *
import random
import time
import decimal

###################################
#classes
###################################
class Day():
    def __init__(self, dayLength, numOfCusts, neededAccuracy):
        self.dayTime = dayLength
        self.numOfCusts = numOfCusts
        self.neededAccuracy = neededAccuracy
        self.custPerTime = dayLength/numOfCusts
        self.custIndex = 0 
        self.custList = [] #list of Customers
    
    def checkIfAddCust(self, app):
        if self.dayTime % self.custPerTime == 0:
            print('new customer')
            self.custList.append(Customer(app))
            
    def checkIfDayOver(self, app):
        if self.dayTime == 0:
            app.mode = 'dayOverScreen'
        else:
            self.dayTime -= 1
            # print(app.currentDay.dayTime)
            
    def incCustWaitTime(self):
        if len(self.custList) != 0:
            for cust in self.custList:
                cust.waitTime += 1
                
    def canNextCust(self, app):
        if self.custIndex < len(self.custList):
            app.isThereCust = True
            app.curCustDrink = self.custList[self.custIndex].order
        else:
            app.isThereCust = False
                    
class Customer():
    def __init__(self, app):
        self.order = []
        self.makeRandomOrder(app)
        self.custImg = ''
        self.getRandomImg(app)
        self.waitTime = 0
        
    def makeRandomOrder(self, app):
        for i in range(5):
            #random.choice from https://www.w3schools.com/python/ref_random_choice.asp
            self.order.append(random.choice(app.OPTIONS[i]))
        # print(self.order)
        
    def getRandomImg(self, app):
        self.custImg = random.choice(app.custImgs)

###################################
#functions
###################################

#evaluation
def resetCustVars(app):
    app.curIng = ''
    app.madeDrinkList = []
    app.madeDrinkDict = dict()
    # app.correctDrinkDict = dict()
    app.tips = 0
    app.cupFullness = 0 #adding up timer
    app.evalRevealTimer = 0
    app.orderRevealTimer = 0
    app.iceCubeCount = 0
    app.sugarCubeCount = 0
    app.hasTakenOrder = False
    app.hasOrder = False
    
def resetDayVars(app):
    app.isThereCust = False
    app.hasTakenOrder = False
    app.hasOrder = False
    resetCustVars(app)

#entire game
def checkIfGameOver(app):
    #check lose condition too
    if app.dayIndex > 7:
        app.mode = 'gameOverScreen'

def startNewDay(app):
    if app.avgScore < .6:
        app.neededAccuracy = 60
    resetDayVars(app)
    app.currentDay = Day(app.dayLength, app.numOfCusts, app.neededAccuracy)
    app.dayIndex += 1

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
    errorMargin = 1-(app.currentDay.neededAccuracy/100)
    correctIngTypes = 0
    goodEnoughIngTime = 0
    wrongIngs = 0
    for ing in app.madeDrinkDict:
        if ing in app.curCustDrink:
            correctIngTypes += 1
            
            if 'milk' in ing:
                correctIngTime = 3
            elif ing in app.toppingsOPTIONS:
                correctIngTime = 4
            elif ing in app.teaOPTIONS:
                correctIngTime = 13
            
            madeIngTime = app.madeDrinkDict[ing]
            highEnd = (1+errorMargin)*correctIngTime
            howFarOff = abs(correctIngTime - madeIngTime)
            ingErrorMargin = highEnd-correctIngTime
            if howFarOff < ingErrorMargin: #within margin of error
                goodEnoughIngTime += 1
        else:
            wrongIngs += 1
            
    #sugar cube score
    correctSugarCubes = int(app.curCustDrink[1][:1])
    if app.sugarCubeCount == correctSugarCubes:
        correctIngTypes += 1
    correctIceCubes = int(app.curCustDrink[2][:1])
    if app.iceCubeCount == correctIceCubes:
        correctIngTypes += 1
        
    #50%-correct ing types
    #30%-accuracy of ing times
    #20%-wait time
    if len(app.madeDrinkDict) != 0:
        app.drinkScore = (correctIngTypes/5)*.5 + (goodEnoughIngTime/3)*.3 + ((500-app.currentDay.custList[app.currentDay.custIndex].waitTime)/500)*.2 # <1
    else:
        app.drinkScore = 0
    #calculate tips
    #drink score must be above 50% to even get any tips
    if app.drinkScore > .5:
        #every second waited = 1 cent less; after 50 seconds = no tips
        app.tips = (500 - app.currentDay.custList[app.currentDay.custIndex].waitTime) *.01 
        app.tips = roundUp(app.tips, 2) #to make it money format
    
    if app.tips > 0:
        app.money += app.tips
    else:
        app.tips = 0   
    
    app.avgScore = (app.avgScore+app.drinkScore)/app.totalOrders # <1
    
###################################   
#general helpers
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

def isValidIngClick(app, x, y, ingCenterTuple):
    x0, y0 = ingCenterTuple[0]-app.ingR, ingCenterTuple[1]-app.ingR
    x1, y1 = ingCenterTuple[0]+app.ingR, ingCenterTuple[1]+app.ingR 
    if (x0 < x < x1) and (y0 < y < y1):
        return True
    return False

#?copied from 15-112 hw8 https://www.cs.cmu.edu/~112/notes/hw8.html 
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#?copied and modified from https://realpython.com/python-rounding/
def roundUp(n, decimals=0):
    multiplier = 10 ** decimals
    return roundHalfUp(n * multiplier) / multiplier

#?copied from TA Mini-Lecture: Advanced Tkinter Mini Lecture
#?https://scs.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f19a16b4-d382-4021-b9e7-af43003eb620
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
    