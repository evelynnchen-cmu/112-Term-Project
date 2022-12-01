from classes import *
###################################
#view
###################################
def evaluationScreen_redrawAll(app, canvas):        
    
    drawBckg(app, canvas)
    drawCust(app, canvas)
    drawMiniTicket(app, canvas)
    drawMiniDrink(app, canvas)
        
    #done button display
    if app.evalRevealTimer > 50:    
        drawButton(canvas, app.eval_doneBtnDms, 'Done')
    
    #side bar stats
    if app.evalRevealTimer > 10:
        drawStats(app, canvas)

def drawBckg(app, canvas):
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
    canvas.create_image(650, 400, image=ImageTk.PhotoImage(scaleImage(app, app.tipsJar, (200, 200))))

def drawCust(app, canvas):
    #customer's body
    canvas.create_image(200, 325, image=ImageTk.PhotoImage(app.body))
    #customer's hairstyle
    canvas.create_image(200, 325, image=ImageTk.PhotoImage(app.currentDay.custList[app.currentDay.custIndex-1].custImg))
    
    #customer's crtique stance
    if app.evalRevealTimer < 20:
        canvas.create_image(200, 325, image=ImageTk.PhotoImage(app.critique))
        
    custReaction = ''
    
    if app.drinkScore*100 > 80:
        custReaction = app.happy
    elif app.drinkScore*100 > 60:
        custReaction = app.neutral
    else:
        custReaction = app.angry
    
    if app.evalRevealTimer > 20:
        #drink score
        canvas.create_image(200, 325, image=ImageTk.PhotoImage(custReaction))

def drawMiniTicket(app, canvas):
    canvas.create_rectangle(275, 415, 347, 496, fill='#eecf90', width=3)
    canvas.create_text(311, 425, text=f"Customer #{(app.currentDay.custIndex)}", font='Courier 6 bold')    
    if len(app.curCustDrink) != 0:
        space = 435
        for ing in app.curCustDrink:
            canvas.create_text(311, space, text=ing, font='Courier 5 bold')
            space += 10

def drawMiniDrink(app, canvas):
    x0 = 411
    x1 = 491
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
    
    #draw ice cubes
    if app.iceCubeCount > 0:
        topOfDrink = 0
        #getting the current top of the drink
        for ing in app.madeDrinkDict:
            topOfDrink += app.madeDrinkDict[ing]
        
        if len(app.madeDrinkList) != 0:
            if app.madeDrinkList[-1] in app.teaOPTIONS or app.madeDrinkList[-1] in app.milkOPTIONS:
                for i in range(app.iceCubeCount):
                    canvas.create_rectangle(425+(11.66*i), 499-(topOfDrink*5), 425+(11.66*(i+1)), 
                                                    499-((topOfDrink*5)-11.66), width=0.1, fill='#C6DCF5')
            elif app.madeDrinkList[-1] in app.toppingsOPTIONS:
                for i in range(app.iceCubeCount):
                    canvas.create_rectangle(425+(11.66*i), 499-(topOfDrink*5)-11.66, 
                                    425+(11.66*(i+1)), 499-(topOfDrink*5), width=0.1, fill='#C6DCF5')
            else:
                for i in range(app.iceCubeCount):
                    canvas.create_rectangle(425+(11.66*i), 487.34, 425+(11.66*(i+1)), 499, width=0.1, fill='#C6DCF5')   
        else:
            for i in range(app.iceCubeCount):
                canvas.create_rectangle(425+(11.66*i), 487.34, 425+(11.66*(i+1)), 499, width=0.1, fill='#C6DCF5')
            
    #cup
    canvas.create_image(450, 449, image=ImageTk.PhotoImage(scaleImage(app, app.cupOutlineGreen, (100, 100))))

#draws sidebar stats
def drawStats(app, canvas):
    if app.evalRevealTimer > 10:
        canvas.create_text(875, 25, text='Order Stats', font='Courier 20 bold underline')
    
    if app.evalRevealTimer > 20:
        
        canvas.create_text(875, 75, text=f'Drink Score: {app.drinkScore*100}%', font='Courier 15 bold')
    
    if app.evalRevealTimer > 30:
        #tips earned
        if len(str(app.tips)) == 3:
            canvas.create_text(875, 125, text=f'Tips Earned: ${app.tips}0', font='Courier 14 bold')
            #tips above tip jar
            canvas.create_text(650, 275, text=f'+${app.tips}0', font='Courier 25 bold')
        else:
            canvas.create_text(875, 125, text=f'Tips Earned: ${app.tips}', font='Courier 14 bold')
            #tips above tip jar
            canvas.create_text(650, 275, text=f'+${app.tips}', font='Courier 25 bold')
        
    
    if app.evalRevealTimer > 40:
        #total average score
        canvas.create_text(875, 175, text=f'Average Score: {app.avgScore*100}%', font='Courier 14 bold')

###################################    
#controller
###################################
def evaluationScreen_mouseReleased(app, event):
    # done button check
    if isValidClick(event.x, event.y, app.eval_doneBtnDms) and app.evalRevealTimer > 50:
        #!still goes to shop be4 day
        if app.currentDay.dayTime <= 0:
            app.mode = 'dayOverScreen'
        app.currentDay.custIndex += 1
        resetCustVars(app)
        app.mode = 'shopScreen'
        
        
def evaluationScreen_timerFired(app):
    app.evalRevealTimer += 1
    app.currentDay.canNextCust(app)
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    checkIfGameOver(app) 