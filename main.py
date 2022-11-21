from cmu_112_graphics import *
from classes import *
from start import *
from dayOver import *
from gameOver import *
from shop import *
from kitchen import *
from evaluation import *
from store import *
#?code/file structure inspired by Vania Halim's 15-112 term project:
#?https://github.com/vaniahalim/15112-TP
###################################
#controller
###################################

def appStarted(app): 
    #?learned about modes from 
    #?https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#usingModes
    app.mode = 'startScreen'
    app.timerDelay = 100
    app.money = 0
    app.tips = 0
    app.totalOrders = 0
    app.neededAccuracy = 70 #will change depending on how good the user is
    app.avgScore = 0 #avg of all the user's scores
    
    #initiailize day variables and start Day 1
    app.dayIndex = 1
    app.dayLength = 1200 #120 seconds
    app.numOfCusts = 20
    app.currentDay = Day(app.dayLength, app.numOfCusts, app.neededAccuracy)
    
    #ordering variables (shopScreen)
    app.curCustImg = ''
    app.isThereCust = False
    app.hasTakenOrder = False
    app.hasOrder = False
    
    #drink variables (kitchenScreen)
    app.curIng = ''
    app.curIngName = 'None'
    app.curCustDrink = ''
    app.madeDrinkList = []
    app.madeDrinkDict = dict()
    app.correctDrinkDict = dict()
    app.startPress = 0
    app.lenOfPress = 0
    app.cupFullness = 0 #adding up timer
    app.isPressed = False
    
    #evaluation variables
    app.drinkScore = 0
    app.tipsDisplay = ''
    
    #reveal timer variables (shopScreen & evaluationScreen)
    app.evalRevealTimer = 0
    app.orderRevealTimer = 0
    
    ###################################
    #inventory
    ###################################
    #starting inventory of ingredients
    app.teaInventory = {"black_tea": 20, "green_tea": 20, "oolong_tea": 20}
    app.toppingsInventory = {"tapioca": 20, "aloe_jelly": 20, "red_bean":20, "pudding": 20}
    app.suppliesInventory = {"cups": 20, "straws": 20, "seals": 20, "milk": 20, "sugar":20}
        
    #ingredient options (used to make random orders)
    app.toppingsOPTIONS = ['tapioca', 'aloe_jelly', 'red_bean', 'pudding']
    app.sugarOPTIONS = ['100%_sugar', '75%_sugar', '50%_sugar', '25%_sugar', '0%_sugar']
    app.iceOPTIONS = ['100%_ice', '75%_ice', '50%_ice', '25%_ice', '0%_ice']
    app.milkOPTIONS = ['whole', '2%', 'skim']
    app.teaOPTIONS = ['black_tea', 'green_tea', 'oolong_tea']
    app.OPTIONS = [app.toppingsOPTIONS, app.sugarOPTIONS, app.iceOPTIONS, app.milkOPTIONS, app.teaOPTIONS]
    
    #ingredient's correct measurements (times)
    app.toppingsTime = {'tapioca': 3, 'aloe_jelly': 3, 'red_bean': 3, 'pudding': 3}
    app.sugarTime = {'100%_sugar': 2, '75%_sugar': 1.5, '50%_sugar': 1, '25%_sugar': .5, '0%_sugar': 0}
    app.iceTime = {'100%_ice': 2, '75%_ice': 1.5, '50%_ice': 1, '25%_ice': .5, '0%_ice': 0}
    app.milkTime = {'whole': 3, '2%': 3, 'skim': 3}
    #!tea don't have specific time bc it'll be whatevers left in the cup
    app.times = [app.toppingsTime, app.sugarTime, app.iceTime, app.milkTime]
    
    
    ###################################
    #buttons
    ###################################
    #startScreen
    app.start_startBtnDms = ((app.width//2)-75, (app.height//2)-25, (app.width//2)+75, (app.height//2)+25)
    
    #shopScreen
    app.shop_takeOrderBtnDms = (app.width*(1/40), app.height*(.6875), app.width*(.175), app.height*(.77))
    app.shop_kitchenBtnDms = (575, 525, 725, 575)
    app.shop_storeBtnDms = (25, 525, 175, 575)
    
    #kitchenScreen
    app.kitchen_storeBtnDms = (25, 525, 175, 575)
    app.kitchen_evalBtnDms = (800, 525, 950, 575)
    app.kitchen_mixBtnDms = (550, 475, 700, 525)
    app.kitchen_addBtnDms = (800, 450, 950, 500)
    
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
    
    
    #evaluationScreen
    app.eval_doneBtnDms = (800, 525, 950, 575)
    
    #storeScreen
    app.store_doneBtnDms = (800, 525, 950, 575)
    
    #dayOverScreen
    app.dayOver_nextDayBtnDms = (800, 525, 950, 575)
    
    #gameOverScreen
    app.gameOver_restartBtnDms = ((app.width//2)-75, (app.height//2)-25, (app.width//2)+75, (app.height//2)+25)
    
    ###################################
    #images
    ###################################
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
    #?drawn by myself on ibisPaint X
    app.evelynn = app.loadImage('./assets/evelynn.png')
    app.happyGuy = app.loadImage('./assets/happy_guy.png')
    app.custImgs = [app.evelynn, app.happyGuy]

runApp(width=1000, height=600, title="Evelynn's Bobaria")
