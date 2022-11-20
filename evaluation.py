from classes import *
#!don't forget to reset drink variables
###################################
#view
###################################
def evaluationScreen_redrawAll(app, canvas):
    tipsJarLarge = scaleImage(app, app.tipsJar, (200, 200))
        
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                fill='black', width=3)
        
    #counter
    canvas.create_line(0, app.height*(5/6), app.width*(3/4), app.height*(5/6), fill='black', width=3)
    canvas.create_rectangle(0, app.height*(5/6), app.width*(3/4), app.height, fill='bisque2')
        
    #tips jar
    canvas.create_image(600, 400, 
                image=ImageTk.PhotoImage(tipsJarLarge))
        
    #drink
    if app.evalRevealTimer > 70:    
        drawButton(canvas, app.eval_doneBtnDms, 'Done')
    
    if app.evalRevealTimer > 20:
        drawStats(app, canvas)
        
def drawStats(app, canvas):
    
    # print(app.tips)
    canvas.create_text(875, 25, text='Order Stats', font='Arial 20 bold underline')
    if app.evalRevealTimer > 30:
        canvas.create_text(875, 75, text=f'Drink Accuracy: {app.drinkAccuracy*100}%', font='Arial 15 bold')
    
    if app.evalRevealTimer > 40:
        #formatting tips
        if app.tips < 1:
            if app.tips % 10 == 0:
                
                canvas.create_text(875, 125, text=f'Tips Earned: ${app.tips}0', font='Arial 15 bold')
            else:
                canvas.create_text(875, 125, text=f'Tips Earned: ${app.tips}', font='Arial 15 bold')
        elif app.tips > 1:
            
            if app.tips % 10 == 0:
                
                canvas.create_text(875, 125, text=f'Tips Earned: ${app.tips}0', font='Arial 15 bold')
                
            else:
                canvas.create_text(875, 125, text=f'Tips Earned: ${app.tips}', font='Arial 15 bold')
    
    if app.evalRevealTimer > 50:
        canvas.create_text(875, 175, text=f'Total Accuracy: {app.totalAccuracy}', font='Arial 15 bold')

###################################    
#controller
###################################
def evaluationScreen_mouseReleased(app, event):
    # done button
    if isValidClick(event.x, event.y, app.eval_doneBtnDms) and app.evalRevealTimer > 70:
        resetCustVars(app)
        app.mode = 'shopScreen'
        
        
def evaluationScreen_timerFired(app):
    app.evalRevealTimer += 1
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    app.currentDay.canNextCust(app)
    
    checkIfGameOver(app)
    
    
    