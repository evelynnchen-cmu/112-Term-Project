from cmu_112_graphics import *
from classes import *
from start import *
from dayOver import *
from gameOver import *
from shop import *
from kitchen import *
from evaluation import *
from store import *
#?code structure inspired by Vania Halim's term project:
#? https://github.com/vaniahalim/15112-TP
###################################
#controller
###################################

def appStarted(app): 
    
    app.mode = 'startScreen'
    app.timerDelay = 100
    app.money = 0
    app.difficulty = 'easy'
    
    #initiailize days
    app.dayLength = 1200 #should be 120 seconds
    app.currentDay = Day(app.dayLength, app.difficulty)
    app.dayIndex = 1
    
    #drink stuff
    app.curIng = ''
    app.curIngName = 'None'
    app.curCustDrink = {'tapioca':400, 'black_tea': 400, '50%_sugar':200, '50%_ice':200, 'whole': 400} # dict()
    app.madeDrinkList = []
    app.madeDrinkDict = dict()
    app.correctDrink = dict()
    app.startPress = 0
    app.lenOfPress = 0
    app.alrAdded = False
    
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
    
    
    app.shop_takeOrderBtnDms = (app.width*(1/40), app.height*(.6875), 
        app.width*(.175), app.height*(.77))
    # app.shop_takeOrderBtnDms = (app.width*(1/40), app.height*(2/3) + app.height*(1/48), 
    #     app.width*(1/10) + app.width*(3/40), app.height*(2/3) + app.height*(1/12) + app.height*(1/48))
    app.shop_kitchenBtnDms = (575, 525, 725, 575)
    app.shop_storeBtnDms = (25, 525, 175, 575)
    
    app.kitchen_storeBtnDms = (25, 525, 175, 575)
    app.kitchen_evalBtnDms = (800, 525, 950, 575)
    
    #ice
    app.kitchen_100iceBtnDms = (25, 50, 100, 100)
    app.kitchen_75iceBtnDms = (125, 50, 200, 100)
    app.kitchen_50iceBtnDms = (25, 110, 100, 160)
    app.kitchen_25iceBtnDms = (125, 110, 200, 160)
    
    #milk
    app.kitchen_wholeMilkBtnDms = (550, 50, 612.5, 100)
    app.kitchen_2pMilkBtnDms = (650, 50, 712.5, 100)
    app.kitchen_skimMilkBtnDms = (600, 115, 662.5, 165)
    
    #sugar
    app.kitchen_100sugarBtnDms = (550, 225, 612.5, 275)
    app.kitchen_75sugarBtnDms = (650, 225, 712.5, 275)
    app.kitchen_50sugarBtnDms = (550, 290, 612.5, 340)
    app.kitchen_25sugarBtnDms = (650, 290, 712.5, 340)
    
    #mix
    app.kitchen_mixBtnDms = (550, 475, 700, 525)
    
    #add
    app.kitchen_addBtnDms = (800, 450, 950, 500)
    
    app.eval_doneBtnDms = (800, 525, 950, 575)
    
    app.store_doneBtnDms = (800, 525, 950, 575)
    
    app.dayOver_nextDayBtnDms = (800, 525, 950, 575)
    
    app.gameOver_restartBtnDms = ((app.width//2)-75, (app.height//2)-25, (app.width//2)+75, (app.height//2)+25)
    
    #images
    #?taken from https://www.freepik.com/premium-vector/tip-jar-semi-flat-color-vector-
    #?object_21941243.htm#page=2&query=tip%20jar&position=11&from_view=keyword
    app.tipsJar = app.loadImage('./assets/tips_jar.png')
    #?taken from https://www.kungfutea.com/our-toppings
    app.tapioca = app.loadImage('./assets/tapioca.png')
    app.aloeJelly = app.loadImage('./assets/aloe_jelly.png')
    app.redBean = app.loadImage('./assets/red_bean.png')
    app.pudding = app.loadImage('./assets/pudding.png')
    #?drawn by myself on OneNote with reference to 
    #?https://www.redbubble.com/es/i/pegatina/Jim-s-Green-Tea-Pot-to-Pam-Kettle-imagen-con-
    #? t%C3%ADtulo-La-oficina-de-zdoehling/35745797.EJUG5
    app.greenTea = app.loadImage('./assets/green_tea.png')
    app.blackTea = app.loadImage('./assets/black_tea.png')
    app.oolongTea = app.loadImage('./assets/oolong_tea.png')

runApp(width=1000, height=600)
