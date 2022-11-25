from classes import *
###################################
#view
###################################
def evaluationScreen_redrawAll(app, canvas):        
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, fill='black', width=3)
        
    #counter
    canvas.create_line(0, app.height*(5/6), app.width*(3/4), app.height*(5/6), fill='black', width=3)
    canvas.create_rectangle(0, app.height*(5/6), app.width*(3/4), app.height, fill='bisque2')
        
    #tips jar
    canvas.create_image(600, 400, image=ImageTk.PhotoImage(scaleImage(app, app.tipsJar, (200, 200))))
    
    #body
    canvas.create_image(200, 325, image=ImageTk.PhotoImage(app.body))
    #customer
    canvas.create_image(200, 325, image=ImageTk.PhotoImage(app.currentDay.custList[app.currentDay.custIndex-1].custImg))

    if app.evalRevealTimer < 20:
        canvas.create_image(200, 325, image=ImageTk.PhotoImage(app.critique))
        
    #done button
    if app.evalRevealTimer > 50:    
        drawButton(canvas, app.eval_doneBtnDms, 'Done')
    
    #side bar stats
    if app.evalRevealTimer > 10:
        drawStats(app, canvas)
        
def drawStats(app, canvas):
    custReaction = ''
    
    if app.drinkScore*100 > 80:
        custReaction = app.happy
    elif app.drinkScore*100 > 60:
        custReaction = app.neutral
    else:
        custReaction = app.angry
    
    canvas.create_text(875, 25, text='Order Stats', font='Courier 20 bold underline')
    if app.evalRevealTimer > 20:
        #drink score
        canvas.create_image(200, 325, image=ImageTk.PhotoImage(custReaction))
        canvas.create_text(875, 75, text=f'Drink Score: {app.drinkScore*100}%', font='Courier 15 bold')
    
    if app.evalRevealTimer > 30:
        #tips earned
        canvas.create_text(875, 125, text=f'Tips Earned: ${app.tips}', font='Courier 15 bold')
    
    if app.evalRevealTimer > 40:
        #total average score
        canvas.create_text(875, 175, text=f'Average Score: {app.avgScore*100}%', font='Courier 15 bold')

###################################    
#controller
###################################
def evaluationScreen_mouseReleased(app, event):
    # done button
    if isValidClick(event.x, event.y, app.eval_doneBtnDms) and app.evalRevealTimer > 50:
        app.currentDay.custIndex += 1
        print(app.currentDay.custIndex)
        resetCustVars(app)
        app.mode = 'shopScreen'
        
        
def evaluationScreen_timerFired(app):
    app.evalRevealTimer += 1
    app.currentDay.canNextCust(app)
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    
    checkIfGameOver(app)
    
    
    