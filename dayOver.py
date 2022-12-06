from classes import *

###################################
#view
###################################
def dayOverScreen_redrawAll(app, canvas):
    drawBckg(app, canvas)
    drawDayResults(app, canvas)
    
    if app.dayOverRevealTimer > 70:
        #next day button display
        if app.hasBrainyBooster:
            canvas.create_image(912.5, 505, image=ImageTk.PhotoImage(app.moneyBoba))
        if app.dayIndex < 7:
            drawButton(canvas, app.dayOver_nextDayBtnDms, 'Next Day')
        else:
            drawButton(canvas, app.dayOver_nextDayBtnDms, 'Game Results')
        drawButton(canvas, app.dayOver_storeBtnDms, 'Store')

def drawBckg(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    canvas.create_image(150, 350, image=ImageTk.PhotoImage(app.boba))
    canvas.create_image(850, 350, image=ImageTk.PhotoImage(app.boba))

def drawDayResults(app, canvas):
    if app.dayOverRevealTimer > 10:
        canvas.create_rectangle(300, 100, 700, 500, fill='#eecf90', width=3)
    
    if app.dayOverRevealTimer > 20:
        canvas.create_text(500, 130, text=f"Day {app.dayIndex} Results", 
                           font='Courier 25 bold underline')
    
    if app.dayOverRevealTimer > 30:
        canvas.create_text(500, 170, text="Number of Customers Served:", 
                           font='Courier 18 bold') 
        
    if app.dayOverRevealTimer > 40:
        canvas.create_text(500, 220, text=f"{app.currentDay.custIndex-1}/{app.currentDay.numOfCusts}", 
                            font='Courier 25 bold')
    
    if app.dayOverRevealTimer > 50:
        canvas.create_text(500, 270, text=f'Average Score:', 
                           font='Courier 18 bold')
        
    if app.dayOverRevealTimer > 60:
        canvas.create_text(500, 320, text=f'{roundUp(app.avgScore*100)}%', 
                           font='Courier 25 bold')
        
    if app.dayOverRevealTimer > 70:
        canvas.create_image(705, 475, image=ImageTk.PhotoImage(app.heartBoba.rotate(angle=-15)))
        if app.avgScore > .8:
            canvas.create_text(500, 400, text=f'Keep it up,\n{app.username}!', font='Courier 25 bold')
        else:
            canvas.create_text(500, 400, text=f'Good effort,\n{app.username}!', font='Courier 25 bold')

###################################    
#controller
###################################
def dayOverScreen_mouseReleased(app, event):
    # next day button check
    if isValidClick(event.x, event.y, app.dayOver_nextDayBtnDms) and app.dayOverRevealTimer > 80:
        saveProgress(app)
        startNewDay(app)
        app.mode = 'shopScreen'
    elif isValidClick(event.x, event.y, app.dayOver_storeBtnDms):
        app.mode = 'storeScreen'
        
def dayOverScreen_timerFired(app):
    app.dayOverRevealTimer += 1    
    
###################################    
#functions
###################################
def saveProgress(app):
    #?adapted from https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
    userInfoDict = ast.literal_eval(readFile('userInfo.txt'))
    
    #if new user, need to add first-time entry
    if app.username not in userInfoDict:
        userInfoDict[app.username] = dict()
    #save user progress
    curUser = userInfoDict[app.username]
    curUser['dayIndex'] = app.dayIndex
    curUser['neededAccuracy'] = app.neededAccuracy 
    curUser['avgScore'] = app.avgScore 
    curUser['lastDaysScore'] = app.lastDaysScore
    curUser['numOfCusts'] = app.numOfCusts
    curUser['money'] = app.money
    curUser['totalOrders'] = app.totalOrders
    curUser['totalScore'] = app.totalScore
    curUser['brainyBooster'] = app.hasBrainyBooster
    curUser['accuracyBooster'] = app.hasAccuracyBooster
    curUser['chefBooster'] = app.hasChefBooster
    
    #?adapted from https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
    writeFile('userInfo.txt', repr(userInfoDict))
    
    