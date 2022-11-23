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
    #!combine these two l8r maybe
    app.curIng = ''
    app.curIngName = 'None'
    app.curCustDrink = ''
    app.madeDrinkList = []
    app.madeDrinkDict = dict()
    app.correctDrinkDict = dict()
    app.drinkScore = 0 #used in evaluation
    app.startAdd = 0
    app.lenOfAdd = 0
    app.cupFullness = 0 #adding up timer
    app.isPressed = False
    
    #drag and drop variables
    app.itemAtRest = True
    app.hasItem = False
    app.isLegal = False
    app.x = app.width//2
    app.y = app.height//2
    
    #reveal timer variables (shopScreen & evaluationScreen)
    app.evalRevealTimer = 0
    app.orderRevealTimer = 70 #!should be 0
    
    ###################################
    #inventory
    ###################################
    #starting inventory of ingredients
    app.teaInventory = {"black_tea": 20, "green_tea": 20, "oolong_tea": 20}
    app.toppingsInventory = {"tapioca": 20, "aloe_jelly": 20, "red_bean":20, "pudding": 20}
    app.suppliesInventory = {"cups": 20, "straws": 20, "seals": 20, "milk": 20, "sugar":20}
        
    #ingredient options (used to make random orders)
    app.toppingsOPTIONS = ['tapioca', 'aloe_jelly', 'red_bean', 'pudding']
    app.sugarOPTIONS = ['4_sugar_cubes', '3_sugar_cubes', '2_sugar_cubes', '1_sugar_cube', '0_sugar_cubes']
    app.iceOPTIONS = ['4_ice_cubes', '3_ice_cubes', '2_ice_cubes', '1_ice_cube', '0_ice_cubes']
    app.milkOPTIONS = ['whole_milk', '2%_milk', 'skim_milk']
    app.teaOPTIONS = ['black_tea', 'green_tea', 'oolong_tea']
    app.OPTIONS = [app.toppingsOPTIONS, app.sugarOPTIONS, app.iceOPTIONS, app.milkOPTIONS, app.teaOPTIONS]
    
    # #ingredient's correct measurements (times)
    # app.toppingsTime = {'tapioca': 3, 'aloe_jelly': 3, 'red_bean': 3, 'pudding': 3}
    # app.milkTime = {'whole_milk': 3, '2%_milk': 3, 'skim_milk': 3}
    
    app.sugarAmts = {'4_sugar_cubes':4, '3_sugar_cubes':3, '2_sugar_cubes':2, '1_sugar_cube':1, '0_sugar_cubes':0}
    app.iceAmts = {'4_ice_cubes':4, '3_ice_cubes':3, '2_ice_cubes':2, '1_ice_cube':1, '0_ice_cubes':0}
    #!tea don't have specific time bc it'll be whatevers left in the cup
    # app.times = [app.toppingsTime, app.milkTime]
    app.amts = [app.sugarAmts, app.iceAmts]
    
    
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
    
    #ing centers
    #!combine these two l8r maybe
    app.sugarCubeCount = 0
    app.iceCubeCount = 0
    app.curIngImg = ''
    app.ingR = 37.5
    app.tapiocaC = (50, 100)
    app.aloeJellyC = (150, 100)
    app.redBeanC = (250, 100)
    app.puddingC = (350, 100)
    
    app.sugarCubeC = (200, 200)
    app.iceCubeC = (200, 300)
    
    app.wholeMilkC = (100, 400)
    app.twoPMilkC = (200, 400)
    app.skimMilkC = (300, 400)
    
    app.greenTeaC = (100, 500)
    app.blackTeaC = (200, 500)
    app.oolongTeaC = (300, 500)
    
    app.ingCs = [app.tapiocaC, app.aloeJellyC, app.redBeanC, app.puddingC, 
                 app.sugarCubeC, app.iceCubeC, app.wholeMilkC, app.twoPMilkC, 
                 app.skimMilkC, app.greenTeaC, app.blackTeaC, app.oolongTeaC]
    
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
    #?drawn by myself on Procreate
    app.tapioca = app.loadImage('./assets/tapioca.png')
    app.aloeJelly = app.loadImage('./assets/aloe_jelly.png')
    app.redBean = app.loadImage('./assets/red_bean.png')
    app.pudding = app.loadImage('./assets/pudding.png')
    app.greenTea = app.loadImage('./assets/green_tea.png')
    app.blackTea = app.loadImage('./assets/black_tea.png')
    app.oolongTea = app.loadImage('./assets/oolong_tea.png')
    app.wholeMilk = app.loadImage('./assets/whole_milk.png')
    app.twoPMilk = app.loadImage('./assets/2p_milk.png')
    app.skimMilk = app.loadImage('./assets/skim_milk.png')
    app.sugarCube = app.loadImage ('./assets/sugar_cube.png')
    app.iceCube = app.loadImage ('./assets/ice_cube.png')
    
    app.ingImgs = [app.tapioca, app.aloeJelly, app.redBean, app.pudding, 
                 app.sugarCube, app.iceCube, app.wholeMilk, app.twoPMilk, 
                 app.skimMilk, app.greenTea, app.blackTea, app.oolongTea]
    
    app.evelynn = app.loadImage('./assets/evelynn.png')
    app.happyGuy = app.loadImage('./assets/guy.png')
    app.custImgs = [app.evelynn, app.happyGuy]

runApp(width=1000, height=600, title="Evelynn's Bobaria")
