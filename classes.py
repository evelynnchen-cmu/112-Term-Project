from cmu_112_graphics import *
import random
import time

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
    app.curIngName = 'None'
    app.madeDrinkList = []
    app.madeDrinkDict = dict()
    app.correctDrinkDict = dict()
    app.startPress = 0
    app.lenOfPress = 0
    app.cupFullness = 0 #adding up timer
    app.evalRevealTimer = 0
    app.orderRevealTimer = 0
    app.hasTakenOrder = False
    app.hasOrder = False

#entire game


def checkIfGameOver(app):
    #check lose condition too
    if app.dayIndex > 7:
        app.mode = 'gameOverScreen'

def startNewDay(app):
    if app.money < 0:
        app.neededAccuracy = 60
    app.currentDay = Day(app.dayLength, app.numOfCusts, app.neededAccuracy)
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
    errorMargin = 1-(app.currentDay.neededAccuracy/100)
    
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
    
    correctIngTypes = 0
    goodEnoughIngTime = 0
    for ing in app.correctDrinkDict:
        
        if ing in app.madeDrinkDict:
            
            # print(f'yes, {ing} in {app.madeDrinkDict}')
            
            correctIngTypes += 1
            madeIngTime = app.madeDrinkDict[ing]
            correctIngTime = app.correctDrinkDict[ing]
            highEnd = (1+errorMargin)*correctIngTime
            howFarOff = abs(correctIngTime - madeIngTime)
            ingErrorMargin = highEnd-correctIngTime
            if howFarOff < ingErrorMargin: #within margin of error
                goodEnoughIngTime += 1
            # else:  
            #     pityPoints = 1
            #     pityPoints -= howFarOff/
                
                # pityPoints = abs(abs(madeIngTime - correctIngTime) - errorMargin)
                # print(f'pityPoints {pityPoints}')
                # goodEnoughIngTime += pityPoints/errorMargin
                # print(goodEnoughIngTime)
            app.drinkAccuracy = ((correctIngTypes/5)*.5 + (goodEnoughIngTime/5)*.5) # <1
       
    # app.totalAccuracy = (app.totalAccuracy+app.drinkAccuracy)/#will be num of completed orders
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
    