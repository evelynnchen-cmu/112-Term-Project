from cmu_112_graphics import *
from classes import *
from start import *
from shop import *
from kitchen import *
from evaluation import *
from store import *
from helpers import *

###################################
#controller
###################################
def appStarted(app): 
    
    app.mode = 'startScreen'
    app.timerDelay = 1000
    app.money = 0
    
    #initiailize days
    app.currentDay = 1
    
    #drink stuff
    app.curCustDrink = dict()
    app.madeDrink = dict()
    app.correctDrink = dict()
    
    #evaluating
    app.correctIng = 0
    app.correctProportions = 0 
    app.drinkAccuracy = 0
    
    #will change depending on how good the user is
    app.neededAccuracy = 70 
    
    #running total of all the user's accuracies
    app.totalAccuracy = 0
    
    #inventory
    app.teaInventory = {"black_tea": 20, "green_tea": 20, "oolong_tea": 20}
    app.toppingsInventory = {"tapioca": 20, "aloe_jelly": 20, "red_bean":20, "pudding": 20}
    app.suppliesInventory = {"cups": 20, "straws": 20, "seals": 20}
        
        #never change
    app.teaOPTIONS = ['black', 'green', 'oolong']
    app.toppingsOPTIONS = ['tapioca', 'aloe_jelly', 'red_bean', 'pudding']
    app.sugarOPTIONS = ['100%_sugar', '75%_sugar', '50%_sugar', '25%_sugar', '0%_sugar']
    app.iceOPTIONS = ['100%_ice', '75%_ice', '50%_ice', '25%_ice', '0%_ice']
    app.milkOPTIONS = ['whole', '2%', 'skim']
    
    #buttons
    app.start_startBtnDms = ((app.width//2)-75, (app.height//2)-25, (app.width//2)+75, (app.height//2)+25)
    
    app.shop_takeOrderBtnDms = (25, 412.5, 175, 462.5)
    app.shop_kitchenBtnDms = (575, 525, 725, 575)
    app.shop_storeBtnDms = (25, 525, 175, 575)
    
    app.kitchen_storeBtnDms = (25, 525, 175, 575)
    app.kitchen_evalBtnDms = (800, 525, 950, 575)
    
    app.eval_doneBtnDms = (800, 525, 950, 575)
    
    app.store_doneBtnDms = (800, 525, 950, 575)
    
    #images
    app.tipsJar = app.loadImage('./assets/tips_jar.png')
    app.tapioca = app.loadImage('./assets/tapioca.png')
    app.aloeJelly = app.loadImage('./assets/aloe_jelly.png')
    app.redBean = app.loadImage('./assets/red_bean.png')
    app.pudding = app.loadImage('./assets/pudding.png')
    app.greenTea = app.loadImage('./assets/green_tea.png')
    app.blackTea = app.loadImage('./assets/black_tea.png')
    app.oolongTea = app.loadImage('./assets/oolong_tea.png')

runApp(width=1000, height=600)
