from classes import *

###################################
#view
###################################
def gameOverScreen_redrawAll(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    
    #stats
    canvas.create_text(500, 50, text=f"Game Statistics", font='Courier 30 bold underline')
    canvas.create_text(500, 100, 
        text=f"Total Number of Customers Served: {app.totalOrders}", 
                        font='Courier 20')
    canvas.create_text(500, 150, text=f'Average Score: {app.avgScore*100}', font='Courier 20')
    canvas.create_text(500, 200, text=f'Total Tips: {app.money}', font='Courier 20')
    
    canvas.create_image(505, 450, image=ImageTk.PhotoImage(app.logo))
    
    #restart button display
    drawButton(canvas, app.gameOver_restartBtnDms, 'Restart')

###################################    
#controller
###################################
def gameOverScreen_mouseReleased(app, event):
    # restart button check
    if isValidClick(event.x, event.y, app.gameOver_restartBtnDms):
        #!reset whole game
        #reset accuracy to starting accuracy
        app.neededAccuracy = 70 
    
        #reset user's running avg score
        app.avgScore = 0
        
        #reset user's money
        app.money = 0
        
        app.totalScore = 0
        app.totalOrders = 0
        
        #reset default number of customers
        app.numOfCusts = 3
        
        #reset difficulty
        app.neededAccuracy = 70
        
        #reset inventory
        # app.teaInventory = {"black_tea": 20, "green_tea": 20, "oolong_tea": 20}
        # app.toppingsInventory = {"tapioca": 20, "aloe_jelly": 20, "red_bean":20, "pudding": 20}
        # app.suppliesInventory = {"cups": 20, "straws": 20, "seals": 20}

        #reset day count
        app.dayIndex = 1
        app.currentDay = Day(app.dayLength, app.numOfCusts, app.neededAccuracy)
        
        resetCustVars(app)
        resetDayVars(app)
        
        app.mode = 'shopScreen'