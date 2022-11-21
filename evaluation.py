from classes import *
#!0% ice and 0% sugar scoring bug
###################################
#view
###################################
def evaluationScreen_redrawAll(app, canvas):
    tipsJarLarge = scaleImage(app, app.tipsJar, (200, 200))
        
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, fill='black', width=3)
        
    #counter
    canvas.create_line(0, app.height*(5/6), app.width*(3/4), app.height*(5/6), fill='black', width=3)
    canvas.create_rectangle(0, app.height*(5/6), app.width*(3/4), app.height, fill='bisque2')
        
    #tips jar
    canvas.create_image(600, 400, 
                image=ImageTk.PhotoImage(tipsJarLarge))
        
    #done button
    if app.evalRevealTimer > 50:    
        drawButton(canvas, app.eval_doneBtnDms, 'Done')
    
    #side bar stats
    if app.evalRevealTimer > 10:
        drawStats(app, canvas)
        
def drawStats(app, canvas):
    
    canvas.create_text(875, 25, text='Order Stats', font='Arial 20 bold underline')
    if app.evalRevealTimer > 20:
        #drink score
        canvas.create_text(875, 75, text=f'Drink Score: {app.drinkScore*100}%', font='Arial 15 bold')
    
    if app.evalRevealTimer > 30:
        #tips earned
        canvas.create_text(875, 125, text=f'Tips Earned: {app.tipsDisplay}', font='Arial 15 bold')
    
    if app.evalRevealTimer > 40:
        #total average score
        canvas.create_text(875, 175, text=f'Average Score: {app.avgScore*100}%', font='Arial 15 bold')

###################################    
#controller
###################################
def evaluationScreen_mouseReleased(app, event):
    # done button
    if isValidClick(event.x, event.y, app.eval_doneBtnDms) and app.evalRevealTimer > 50:
        app.currentDay.custIndex += 1
        resetCustVars(app)
        app.mode = 'shopScreen'
        
        
def evaluationScreen_timerFired(app):
    app.evalRevealTimer += 1
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    app.currentDay.canNextCust(app)
    checkIfGameOver(app)
    
    
    