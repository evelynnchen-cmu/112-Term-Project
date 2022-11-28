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
    
    #----overall game----
    app.timerDelay = 100
    app.money = 0
    app.tips = 0
    #avg of all the user's scores
    app.avgScore = 0 
    app.totalOrders = 0
    #will change depending on how good the user is
    app.neededAccuracy = 70 
    
    #----day variables----
    #day 1
    app.dayIndex = 1
    app.dayLength = 1200 #!120 seconds
    app.numOfCusts = 3
    app.currentDay = Day(app.dayLength, app.numOfCusts, app.neededAccuracy)
    app.lastDaysScore = 0
    
    #----ordering variables----
    app.curCustImg = ''
    app.isThereCust = False
    app.hasTakenOrder = False
    app.hasOrder = False
    
    #----drink variables----
    app.curIng = ''
    app.curIngName = 'None'
    app.curCustDrink = ''
    app.madeDrinkList = []
    app.madeDrinkDict = dict()
    app.correctDrinkDict = dict()
    app.drinkScore = 0
    app.startAdd = 0
    app.lenOfAdd = 0
    app.cupFullness = 0
    app.sugarY = 0
    app.randomSpot = 0
    app.isAdding = False
    app.isMixed = False
    
    #----moving ingredients variables----
    app.x = app.width//2
    app.y = app.height//2
    app.itemAtRest = True
    app.hasItem = False
    app.isLegal = False
    app.entered = False
    app.isRotated = False
    
    #reveal timer variables
    app.evalRevealTimer = 0
    app.orderRevealTimer = 70 #!should be 0
    
    # #inventory
    # #starting inventory of ingredients
    # app.teaInventory = {"black_tea": 20, "green_tea": 20, "oolong_tea": 20}
    # app.toppingsInventory = {"tapioca": 20, "aloe_jelly": 20, "red_bean":20, "pudding": 20}
    # app.suppliesInventory = {"cups": 20, "straws": 20, "seals": 20, "milk": 20, "sugar":20}
        
    #----ingredients----
    app.ings = ['tapioca', 'aloe_jelly', 'red_bean', 'pudding', 'sugarCube', 
                'iceCube', 'whole_milk', '2%_milk', 'skim_milk', 'green_tea', 
                'black_tea', 'oolong_tea']
    
    app.toppingsOPTIONS = ['tapioca', 'aloe_jelly', 'red_bean', 'pudding']
    app.sugarOPTIONS = ['4_sugar_cubes', '3_sugar_cubes', '2_sugar_cubes', '1_sugar_cube', '0_sugar_cubes']
    app.iceOPTIONS = ['4_ice_cubes', '3_ice_cubes', '2_ice_cubes', '1_ice_cube', '0_ice_cubes']
    app.milkOPTIONS = ['whole_milk', '2%_milk', 'skim_milk']
    app.teaOPTIONS = ['black_tea', 'green_tea', 'oolong_tea']
    app.OPTIONS = [app.toppingsOPTIONS, app.sugarOPTIONS, app.iceOPTIONS, app.milkOPTIONS, app.teaOPTIONS]
    
    app.tapiocaC, app.aloeJellyC, app.redBeanC, app.puddingC = (50, 100), (150, 100), (250, 100), (350, 100)
    app.sugarCubeC, app.iceCubeC = (200, 200), (200, 300)
    app.wholeMilkC, app.twoPMilkC, app.skimMilkC = (100, 400), (200, 400), (300, 400)
    app.greenTeaC, app.blackTeaC, app.oolongTeaC = (100, 500), (200, 500), (300, 500) 
    app.ingCs = [app.tapiocaC, app.aloeJellyC, app.redBeanC, app.puddingC, 
                 app.sugarCubeC, app.iceCubeC, app.wholeMilkC, app.twoPMilkC, 
                 app.skimMilkC, app.greenTeaC, app.blackTeaC, app.oolongTeaC]
    
    app.curIngImg = ''
    app.sugarCubeCount = 0
    app.iceCubeCount = 0
    app.ingR = 37.5
    
    #----startScreen button----
    app.start_startBtnDms = (425, 300, 575, 350)
    
    #----shopScreen buttons----
    app.shop_takeOrderBtnDms = (25, 412.5, 175, 462)
    app.shop_kitchenBtnDms = (800, 425, 950, 475)
    app.shop_storeBtnDms = (25, 525, 175, 575)
    
    #----kitchenScreen buttons----
    app.kitchen_storeBtnDms = (25, 525, 175, 575)
    app.kitchen_evalBtnDms = (800, 525, 950, 575)
    app.kitchen_mixBtnDms = (800, 425, 950, 475)
    
    #----evaluationScreen button----
    app.eval_doneBtnDms = (800, 525, 950, 575)
    
    #----storeScreen button----
    app.store_doneBtnDms = (800, 525, 950, 575)
    
    #----dayOverScreen button----
    app.dayOver_nextDayBtnDms = (425, 275, 575 , 325)
    
    #----gameOverScreen button----
    app.gameOver_restartBtnDms = ((app.width//2)-75, (app.height//2)-25, (app.width//2)+75, (app.height//2)+25)
    
    #----images----
    #?drawn by myself on Procreate
    #----ingredients----
    app.tapioca = app.loadImage('./assets/ingredients/tapioca.png')
    app.aloeJelly = app.loadImage('./assets/ingredients/aloe_jelly.png')
    app.redBean = app.loadImage('./assets/ingredients/red_bean.png')
    app.pudding = app.loadImage('./assets/ingredients/pudding.png')
    app.greenTea = app.loadImage('./assets/ingredients/green_tea.png')
    app.blackTea = app.loadImage('./assets/ingredients/black_tea.png')
    app.oolongTea = app.loadImage('./assets/ingredients/oolong_tea.png')
    app.wholeMilk = app.loadImage('./assets/ingredients/whole_milk.png')
    app.twoPMilk = app.loadImage('./assets/ingredients/2p_milk.png')
    app.skimMilk = app.loadImage('./assets/ingredients/skim_milk.png')
    app.sugarCube = app.loadImage ('./assets/ingredients/sugar_cube.png')
    app.iceCube = app.loadImage ('./assets/ingredients/ice_cube.png')
    app.ingImgs = [app.tapioca, app.aloeJelly, app.redBean, app.pudding, 
                 app.sugarCube, app.iceCube, app.wholeMilk, app.twoPMilk, 
                 app.skimMilk, app.greenTea, app.blackTea, app.oolongTea]
    
    
    #----customers----
    #?drawn by myself on Procreate
    app.body = app.loadImage('./assets/customers/stances/body.png')
    app.neutral = app.loadImage('./assets/customers/stances/neutral.png')
    
    #----reactions----
    app.happy = app.loadImage('./assets/customers/stances/happy.png')
    app.critique = app.loadImage('./assets/customers/stances/critique.png')
    app.angry = app.loadImage('./assets/customers/stances/angry.png')
    
    #----hairstyles----
    app.bangs = app.loadImage('./assets/customers/bangs.png')
    app.boring = app.loadImage('./assets/customers/boring.png')
    app.emo = app.loadImage('./assets/customers/emo.png')
    app.grandma = app.loadImage('./assets/customers/grandma.png')
    app.grandpa = app.loadImage('./assets/customers/grandpa.png')
    app.leoDicaprio = app.loadImage('./assets/customers/leo_dicaprio.png')
    app.longCurlyHair = app.loadImage('./assets/customers/long_curly_hair.png')
    app.longHair = app.loadImage('./assets/customers/long_hair.png')
    app.longStraightHair = app.loadImage('./assets/customers/long_straight_hair.png')
    app.shortCurlyHair = app.loadImage('./assets/customers/short_curly_hair.png')
    app.custImgs = [app.bangs, app.boring, app.emo, app.grandma, app.grandpa, 
                    app.leoDicaprio, app.longCurlyHair, app.longHair, app.longStraightHair,
                    app.shortCurlyHair]
    
    #----decorations----
    app.tipsJar = app.loadImage('./assets/decorations/tips_jar.png')
    app.cupOutlineGray = app.loadImage('./assets/decorations/cup_outline_gray.png')
    app.cupOutlineGreen = app.loadImage('./assets/decorations/cup_outline_green.png')
    app.logo = app.loadImage('./assets/decorations/logo.png')
    app.boba = app.loadImage('./assets/decorations/boba.png')
    app.cashRegister = app.loadImage('./assets/decorations/cash_register.png')
    app.counter = app.loadImage('./assets/decorations/counter.png')
    
    #?taken from https://www.istockphoto.com/es/vector/t%C3%A9-de-burbujas-popular-
    #?t%C3%A9-de-leche-de-perla-taiwan%C3%A9s-con-bolas-t%C3%A9-asi%C3%A1tico-burbuja-
    #?gm1273459736-375324413
    app.cashRegisterScreen = app.loadImage('./assets/decorations/cash_register_screen.jpg')

runApp(width=1000, height=600, title="Evelynn's Bobaria")
