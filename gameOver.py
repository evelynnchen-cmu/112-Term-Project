from classes import *

###################################
#view
###################################
def gameOverScreen_redrawAll(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    
    drawButton(canvas, app.gameOver_restartBtnDms, 'Restart')
    
    #trademark
    canvas.create_image(965, 555, image=ImageTk.PhotoImage(scaleImage(app, app.logo, (75, 75))))

###################################    
#controller
###################################
def gameOverScreen_mouseReleased(app, event):
    # restart button
    if isValidClick(event.x, event.y, app.gameOver_restartBtnDms):
        #!reset whole game
        #reset accuracy to starting accuracy
        app.neededAccuracy = 70 
    
        #reset user's running avg score
        app.avgScore = 0
        
        #reset user's money
        app.money = 0
        
        #reset difficulty
        app.neededAccuracy = 70
        
        #reset inventory
        app.teaInventory = {"black_tea": 20, "green_tea": 20, "oolong_tea": 20}
        app.toppingsInventory = {"tapioca": 20, "aloe_jelly": 20, "red_bean":20, "pudding": 20}
        app.suppliesInventory = {"cups": 20, "straws": 20, "seals": 20}

        app.currentDay = Day(app.dayLength, app.difficulty)
        #reset day count
        app.dayIndex = 1
        app.mode = 'shopScreen'