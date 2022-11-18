from classes import *

###################################
#view
###################################
def gameOverScreen_redrawAll(app, canvas):
    drawButton(canvas, app.gameOver_restartBtnDms, 'Restart')

###################################    
#controller
###################################
def gameOverScreen_mouseReleased(app, event):
    # restart button
    if isValidClick(event.x, event.y, app.gameOver_restartBtnDms):
        #!reset whole game
        #reset accuracy to starting accuracy
        app.neededAccuracy = 70 
    
        #reset user's total accuracy
        app.totalAccuracy = 0
        
        #reset user's money
        app.money = 0
        
        #reset difficulty
        app.difficulty = 'easy'
        
        #reset inventory
        app.teaInventory = {"black_tea": 20, "green_tea": 20, "oolong_tea": 20}
        app.toppingsInventory = {"tapioca": 20, "aloe_jelly": 20, "red_bean":20, "pudding": 20}
        app.suppliesInventory = {"cups": 20, "straws": 20, "seals": 20}

        app.currentDay = Day(app.dayLength, app.difficulty)
        #reset day count
        app.dayIndex = 1
        app.mode = 'shopScreen'