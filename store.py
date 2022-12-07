from classes import *

###################################
#view
###################################
def storeScreen_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    canvas.create_text(500, 25, text='Boba Baby Booster Store', font='Courier 25 bold')
    canvas.create_text(105, 25, text=f'Tips: ${roundUp(app.money, 2)}', font='Courier 20 bold')
    
    if app.hasBrainyBooster and app.hasAccuracyBooster and app.hasChefBooster:
        canvas.create_text(500, 300, text='You bought all the Boba Baby Boosters!', font='Courier 20 bold')
    else:
        canvas.create_text(240, 100, text='Boosters Available', font='Courier 20 bold')
    
    #exit button display
    drawButton(canvas, app.store_exitBtnDms, 'Exit')
    
    #help boba display
    canvas.create_image(30, 550, image=ImageTk.PhotoImage(scaleImage(app, app.helpBoba, (100, 75))))
    
    drawBoosters(app, canvas)
    drawDescs(app, canvas)
    
    if app.curSelection != '':
        if ((app.curSelection == 'brainyBooster' and app.money > 10) or 
            (app.curSelection == 'accuracyBooster' and app.money > 15) or
            (app.curSelection == 'chefBooster' and app.money > 20)):
            #buy button display
            pass
    
def drawBoosters(app, canvas):
    if not app.hasBrainyBooster:
        #money boba baby booster
        canvas.create_text(250, 315, text="Brainy", font='Courier 17 bold')
        canvas.create_image(250, 200, image=ImageTk.PhotoImage(scaleImage(app, app.moneyBoba, (225, 225))))
    
    if not app.hasAccuracyBooster:
        #accuracy boba baby booster
        canvas.create_text(150, 550, text='Inspector', font='Courier 17 bold')
        canvas.create_image(150, 425, image=ImageTk.PhotoImage(scaleImage(app, app.searchingBoba, (250, 250))))
    
    if not app.hasChefBooster:
        #chef boba baby booster
        canvas.create_text(350, 550, text='Mini-Chef', font='Courier 17 bold')
        canvas.create_image(350, 425, image=ImageTk.PhotoImage(scaleImage(app, app.chefBoba, (250, 250))))
    
def drawDescs(app, canvas):
    if app.curSelection == 'brainyBooster' and not app.hasBrainyBooster:
        canvas.create_text(700, 100, text='Booster Description', font='Courier 20 bold')
        canvas.create_rectangle(500, 125, 900, 400, width=3, fill='#bab2d9')
        canvas.create_text(635, 225, text="""
            The 'Brainy' Boba Baby Booster
            keeps customers entertained 
            while you make their drink. This 
            makes them more lenient on the 
            wait time, meaning extra tips 
            for you!\n
            Cost: $10
            """, font='Courier 15 bold')
        if app.money > 10:
            drawButton(canvas, app.store_buyBtnDms, 'Buy')
    elif app.curSelection == 'accuracyBooster' and not app.hasAccuracyBooster:
        canvas.create_text(700, 100, text='Booster Description', font='Courier 20 bold')
        canvas.create_rectangle(500, 125, 900, 400, width=3, fill='#bab2d9')
        canvas.create_text(633, 235, text="""
            The 'Inspector' Boba Baby 
            Booster lets the customer know 
            during evaluation how highly 
            accurate you made the drink, 
            making the customer not inspect 
            it as thoroughly before giving a 
            score.\n
            Cost: $15
            """, font='Courier 15 bold')
        if app.money > 15:
            drawButton(canvas, app.store_buyBtnDms, 'Buy')
    elif app.curSelection == 'chefBooster' and not app.hasChefBooster:
        canvas.create_text(700, 100, text='Booster Description', font='Courier 20 bold')
        canvas.create_rectangle(500, 125, 900, 400, width=3, fill='#bab2d9')
        canvas.create_text(632, 225, text="""
            The 'Mini-Chef' Boba Baby 
            Booster makes sure you have the 
            recommended ingredient fill 
            lines for the rest of the game, 
            that way you can be as accurate 
            as possible!\n
            Cost: $20 
            """, font='Courier 15 bold')
        if app.money > 20:
            drawButton(canvas, app.store_buyBtnDms, 'Buy')
###################################    
#controller
###################################
def storeScreen_mouseReleased(app, event):
    x, y = event.x, event.y
    # clicked on brainy booster check
    if isValidClick(x, y, (140, 125, 360, 305)):
        app.curSelection = 'brainyBooster'
    # clicked on accuracy booster check
    elif isValidClick(x , y, (65, 385, 225, 540)):
        app.curSelection = 'accuracyBooster'
    # clicked on chef booster chek
    elif isValidClick(x, y, (265, 320, 440, 540)):
        app.curSelection = 'chefBooster'
    # exit button check
    if isValidClick(x, y, app.store_exitBtnDms):
        app.mode = 'dayOverScreen'
    # help boba check
    elif isValidClick(x, y, (3, 517, 53, 587)):
        app.curHelpScene = 5
        app.cameFromGame = True
        app.mode = 'helpScreen'
    elif isValidClick(x, y, app.store_buyBtnDms) and app.curSelection != '':
        canBuy(app)
    
    
###################################    
#functions
###################################
def canBuy(app):
    if app.curSelection == 'brainyBooster':
        cost = 10
        if cost <= app.money and not app.hasBrainyBooster:
            app.money -= cost
            app.hasBrainyBooster = True
    elif app.curSelection == 'accuracyBooster':
        cost = 15
        if cost <= app.money and not app.hasAccuracyBooster:
            app.money -= cost
            app.hasAccuracyBooster = True
    elif app.curSelection == 'chefBooster':
        cost = 20
        if cost <= app.money and not app.hasChefBooster:
            app.money -= cost
            app.hasChefBooster = True