from cmu_112_graphics import *
from classes import *
from start import *
from shop import *
from kitchen import *
from evaluation import *
from store import *
from helpers import *

def appStarted(app): 
    
    app.mode = 'startScreen'
    app.timerDelay = 1000
    
    app.day1 = Day(app)
    app.day2 = Day(app)
    app.day3 = Day(app)
    app.day4 = Day(app)
    app.day5 = Day(app)
    app.day6 = Day(app)
    app.day7 = Day(app)

    app.days = [app.day1, app.day2, app.day3, app.day4, app.day5, app.day6, app.day7]
    app.currentDay = 1
    app.money = 0
    
    #inventory
    app.teaInventory = {"black_tea": 20, "green_tea": 20, "oolong_tea": 20}
    app.toppingsInventory = {"tapioca": 20, "lychee": 20, "red_bean":20, "pudding": 20}
    app.suppliesInventory = {"cups": 20, "straws": 20, "seals": 20}
        
        #never change
    app.teaOPTIONS = ['black', 'green', 'oolong']
    app.toppingsOPTIONS = ['tapioca', 'lychee', 'red_bean', 'pudding']
    app.sugarOPTIONS = ['100%', '75%', '50%', '25%', '0%']
    app.iceOPTIONS = ['100%', '75%', '50%', '25%', '0%']
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

runApp(width=1000, height=600)
