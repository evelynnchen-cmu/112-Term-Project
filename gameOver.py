from classes import *

###################################
#view
###################################
def gameOverScreen_redrawAll(app, canvas):
    drawBckg(app, canvas)
    drawGameResults(app, canvas)
    
    if app.gameOverRevealTimer > 90:
        #restart button display
        drawButton(canvas, app.gameOver_restartBtnDms, 'Restart')
        
        #exit button display
        drawButton(canvas, app.gameOver_exitBtnDms, 'Exit')

def drawBckg(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    
    canvas.create_image(150, 350, image=ImageTk.PhotoImage(app.logo))
    canvas.create_image(850, 350, image=ImageTk.PhotoImage(app.logo))
    
    #cover bobas' mouths
    canvas.create_rectangle(125, 335, 150, 350, fill='#ceb195', width=0)
    canvas.create_rectangle(825, 335, 850, 350, fill='#ceb195', width=0)

def drawGameResults(app, canvas):
    if app.gameOverRevealTimer > 10:
        canvas.create_rectangle(300, 100, 700, 500, fill='#eecf90', width=3)
    
    if app.gameOverRevealTimer > 20:
        canvas.create_text(500, 130, text=f"Game Results", font='Courier 25 bold underline')
    
    if app.gameOverRevealTimer > 30:
        canvas.create_text(501, 170, text="Total Number of Customers Served:", font='Courier 15 bold') 
        
    if app.gameOverRevealTimer > 40:
        canvas.create_text(500, 210, text=f"{app.totalOrders}", font='Courier 25 bold')
    
    if app.gameOverRevealTimer > 50:
        canvas.create_text(500, 250, text=f'Average Score:', font='Courier 18 bold')
        
    if app.gameOverRevealTimer > 60:
        canvas.create_text(500, 290, text=f'{app.avgScore*100}%', font='Courier 25 bold')
        
    if app.gameOverRevealTimer > 70:
        canvas.create_text(500, 330, text='Total Tips:', font='Courier 18 bold')
    
    if app.gameOverRevealTimer > 80:
        canvas.create_text(500, 370, text=f'${app.money}', font='Courier 25 bold')
    
    #show if they won or not
    if app.gameOverRevealTimer > 90:
        canvas.create_image(705, 470, image=ImageTk.PhotoImage(app.heartBoba.rotate(angle=-15)))
        #the average score must be above 30% to win
        if app.avgScore < .3:
            canvas.create_text(500, 420, text=f'Better luck next time,\n{app.username}!',
                               font='Courier 25 bold')
            canvas.create_text(150, 200, text='You Lost', font='Courier 25 bold')
            canvas.create_text(850, 200, text='You Lost', font='Courier 25 bold')
            e = 180
        else:
            canvas.create_text(500, 420, text=f'Good job,\n{app.username}!',
                               font='Courier 25 bold')
            canvas.create_text(150, 200, text='You Won!', font='Courier 25 bold')
            canvas.create_text(850, 200, text='You Won!', font='Courier 25 bold')
            e = -180
        #bobas' mouths
        #?adapted from 15-112 hw9 https://www.cs.cmu.edu/~112/notes/hw9.html#freddyFractal
        canvas.create_arc(125, 330, 150, 345,
                        outline="black", width = 3, style="arc", extent=e)
        canvas.create_arc(825, 330, 850, 345,
                        outline="black", width = 3, style="arc", extent=e)

###################################    
#controller
###################################
def gameOverScreen_mouseReleased(app, event):
    # restart button check
    if isValidClick(event.x, event.y, app.gameOver_restartBtnDms) and app.gameOverRevealTimer > 90:
        #reset user's stored data
        resetData(app)
        
        #reset overall game variables
        app.dayIndex = 1
        app.neededAccuracy = 70
        app.avgScore = 0
        app.lastDaysScore = 0
        app.numOfCusts = 3
        app.money = 0
        app.totalOrders = 0
        app.totalScore = 0
        app.patience = 550
        app.hasBrainyBooster = False
        app.hasAccuracyBooster = False
        app.hasChefBooster = False
        app.currentDay = Day(app.dayLength, app.numOfCusts, app.neededAccuracy)
        app.gameOverRevealTimer = 0
        
        app.ings = ['tapioca', 'aloe_jelly', 'red_bean', 'pudding', 'sugarCube', 
                'iceCube', 'whole_milk', '2%_milk', 'skim_milk', 'green_tea', 
                'black_tea', 'oolong_tea']
        app.toppingsOPTIONS = ['tapioca', 'aloe_jelly', 'red_bean', 'pudding']
        app.ingCs = [app.tapiocaC, app.aloeJellyC, app.redBeanC, app.puddingC, 
                 app.sugarCubeC, app.iceCubeC, app.wholeMilkC, app.twoPMilkC, 
                 app.skimMilkC, app.greenTeaC, app.blackTeaC, app.oolongTeaC]
        app.ingImgs = [app.tapioca, app.aloeJelly, app.redBean, app.pudding, 
                 app.sugarCube, app.iceCube, app.wholeMilk, app.twoPMilk, 
                 app.skimMilk, app.greenTea, app.blackTea, app.oolongTea]
        
        resetCustVars(app)
        resetDayVars(app)
        app.mode = 'shopScreen'
    # exit button check
    elif isValidClick(event.x, event.y, app.gameOver_exitBtnDms) and app.gameOverRevealTimer > 90:
        #?copied from cmu_112_graphics.py
        os._exit(0)
        
def gameOverScreen_timerFired(app):
    app.gameOverRevealTimer += 1 

###################################    
#functions
###################################    
def resetData(app):
    #?adapted from https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
    userInfoDict = ast.literal_eval(readFile('userInfo.txt'))
    userInfoDict[app.username] = dict()
    #?adapted from https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
    writeFile('userInfo.txt', repr(userInfoDict))
    