from classes import *
###################################
#view
###################################
def evaluationScreen_redrawAll(app, canvas):        
    
    #background
    canvas.create_rectangle(0, 0, 750, 500, fill='#b2beb5', width=0)
    
    #blue sidebar
    canvas.create_rectangle(750, 0, app.width, app.height, fill='lightblue1', width=0)
    
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, fill='black', width=3)
    
    #counter
    canvas.create_line(0, app.height*(5/6), app.width*(3/4), app.height*(5/6), fill='black', width=3)
    canvas.create_image(375, 600, image=ImageTk.PhotoImage(app.counter))
        
    #tips jar
    canvas.create_image(600, 400, image=ImageTk.PhotoImage(scaleImage(app, app.tipsJar, (200, 200))))
    
    #body
    canvas.create_image(200, 325, image=ImageTk.PhotoImage(app.body))
    #customer
    canvas.create_image(200, 325, image=ImageTk.PhotoImage(app.currentDay.custList[app.currentDay.custIndex-1].custImg))
    
    #trademark
    canvas.create_image(965, 555, image=ImageTk.PhotoImage(scaleImage(app, app.logo, (75, 75))))

    drawMiniDrink(app, canvas)
    
    if app.evalRevealTimer < 20:
        canvas.create_image(200, 325, image=ImageTk.PhotoImage(app.critique))
        
    #done button
    if app.evalRevealTimer > 50:    
        drawButton(canvas, app.eval_doneBtnDms, 'Done')
    
    #side bar stats
    if app.evalRevealTimer > 10:
        drawStats(app, canvas)

def drawMiniDrink(app, canvas):
    # canvas.create_line(360, 400, 440, 400, fill='red')
    # canvas.create_line(360, 500, 440, 500, fill='red')
    x0 = 361
    x1 = 441
    y0 = 499
    y1 = 499
    
    newColor = mixDrink(app)
    mixedDrinkToppings = dict()
    topOfToppings = 0
        
    for ing in app.madeDrinkDict:
        #get dict of only made toppings
        if ing in app.toppingsOPTIONS:
            mixedDrinkToppings[ing] = app.madeDrinkDict[ing]
            topOfToppings += app.madeDrinkDict[ing]

    #draw toppings
    for ing in mixedDrinkToppings:
        color = getIngColor(app, ing)
        addLen = mixedDrinkToppings[ing]*5
        y1 = y0 
        y0 -= addLen
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
    #draw mixed liquid
    canvas.create_rectangle(x0, 499-(app.cupFullness*5), x1, 
                            499-(topOfToppings*5), fill=newColor, width=0)
    canvas.create_image(400, 450, image=ImageTk.PhotoImage(scaleImage(app, app.cupOutlineGreen, (100, 100))))
    
    
    
        
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
        if len(str(app.tips)) == 3:
            canvas.create_text(875, 125, text=f'Tips Earned: ${app.tips}0', font='Courier 15 bold')
        else:
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
    
    
    