from cmu_112_graphics import *
from player import *
from day import *
from customer import *
from shop import *
from kitchen import *
from evaluation import *
from store import *
from inventory import *
from helpers import *

import time

###############################################
#shop screen mode
###############################################
def shopScreen_keyPressed(app, event):
    pass

def shopScreen_mouseReleased(app, event):
    # kitchen button
    if isValidClick(event.x, event.y, app.shop.kitchenBtnDms):
        app.mode = 'kitchenScreen'
    # store button
    elif isValidClick(event.x, event.y, app.shop.storeBtnDms):
        app.mode = 'storeScreen'

def shopScreen_redrawAll(app, canvas):
    app.shop.drawBckg(app, canvas)
    
def shopScreen_timerFired(app):
    print(app.customer.order)
    app.customer.waitTime -= 1
    print(app.customer.waitTime)
    
###############################################
#kitchen screen mode
###############################################
def kitchenScreen_keyPressed(app, event):
    pass

def kitchenScreen_mouseReleased(app, event):
    # store button
    if isValidClick(event.x, event.y, app.kitchen.storeBtnDms):
        app.mode = 'storeScreen'
    # eval button
    elif isValidClick(event.x, event.y, app.kitchen.evalBtnDms):
        app.mode = 'evaluationScreen'

def kitchenScreen_redrawAll(app, canvas):
    app.kitchen.drawBckg(app, canvas)

###############################################
#evaluation screen mode
###############################################
def evaluationScreen_keyPressed(app, event):
    pass

def evaluationScreen_mouseReleased(app, event):
    # done button
    if isValidClick(event.x, event.y, app.evaluation.doneBtnDms):
        app.mode = 'shopScreen'

def evaluationScreen_redrawAll(app, canvas):
    app.evaluation.drawBckg(app, canvas)

###############################################
#store screen mode
###############################################
def storeScreen_keyPressed(app, event):
    if event.key == 'b':
        app.player.money -= 2
        app.inventory.teaInventory['black_tea'] += 1
        

def storeScreen_mouseReleased(app, event):
    # done button
    if isValidClick(event.x, event.y, app.store.doneBtnDms):
        app.mode = 'shopScreen'

def storeScreen_redrawAll(app, canvas):
    app.store.drawBckg(app, canvas)
    app.store.drawInventory(app, canvas)
    app.store.drawOptions(app, canvas)

###############################################
#start screen mode
###############################################
def startScreen_keyPressed(app, event):
    pass

def startScreen_mouseReleased(app, event):
    # start button
    if isValidClick(event.x, event.y, app.startBtnDms):
        app.mode = 'shopScreen'
        app.gameStartTime = time.time()
        app.player.playGame(app)

def startScreen_redrawAll(app, canvas):
    drawButton(canvas, app.startBtnDms, 'Start')

###############################################
#main app
###############################################

def appStarted(app): 
    app.startBtnDms = ((app.width//2)-75, (app.height//2)-25, (app.width//2)+75, (app.height//2)+25)
    app.mode = 'startScreen'
    app.timerDelay = 1000
    app.player = Player(app)
    app.shop = Shop(app)
    app.kitchen = Kitchen(app)
    app.evaluation = Evaluation(app)
    app.store = Store(app)
    app.inventory = Inventory(app)
    
    #will not act be here
    app.customer = Customer(app)

runApp(width=1000, height=600)