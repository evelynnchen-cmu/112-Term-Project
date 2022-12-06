from classes import *

#?method to getting username inspired by 
#?https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#ioMethods
###################################
#view
###################################
def nameScreen_redrawAll(app, canvas):
    #background
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    canvas.create_image(150, 350, image=ImageTk.PhotoImage(app.boba))
    canvas.create_image(850, 350, image=ImageTk.PhotoImage(app.boba))
    
    #title
    canvas.create_text(500, 150, text="Evelynn's Bobaria", font='Courier 50 bold')
    
    #ask for name
    canvas.create_text(500, 250, text='Type in your username to', font='Courier 15 bold')
    canvas.create_text(500, 270, text='start saving or retrieve your progress', font='Courier 15 bold')
    
    #username display
    canvas.create_rectangle(250, 300, 750, 350, width=3, fill='#eecf90')
    canvas.create_text(500, 325, text=app.username, font='Courier 20 bold')
    
def nameScreen_keyPressed(app, event):
            
    if len(app.username) < 15:
        if event.key == 'Enter':
            if checkForProgress(app):
                app.mode = 'shopScreen'
            else:
                app.mode = 'startScreen'
        elif event.key == 'Space':
            app.username += ' '
        elif event.key == 'Backspace':
            app.username = app.username[:-1]
        else:
            app.username += event.key
            
    if event.key == 'Backspace':
            app.username = app.username[:-1]
    
###################################    
#functions
###################################
def checkForProgress(app):
    #?adapted from https://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
    userInfoDict = ast.literal_eval(readFile('userInfo.txt'))
    
    #if user has game progress
    if app.username in userInfoDict:
        curUser = userInfoDict[app.username]
        app.dayIndex = curUser['dayIndex']
        app.neededAccuracy = curUser['neededAccuracy']
        app.avgScore = curUser['avgScore']
        app.lastDaysScore = curUser['lastDaysScore']
        app.numOfCusts = curUser['numOfCusts']
        app.money = curUser['money']
        app.hasBrainyBooster = curUser['brainyBooster'] 
        app.hasAccuracyBooster = curUser['accuracyBooster'] 
        app.hasChefBooster= curUser['chefBooster']
        startNewDay(app)
        return True
    else:
        return False