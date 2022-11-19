from classes import *

###################################
#view
###################################
def kitchenScreen_redrawAll(app, canvas):
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                fill='black', width=3)
        
    drawButton(canvas, app.kitchen_storeBtnDms, 'Store')
    drawButton(canvas, app.kitchen_evalBtnDms, 'Evaluate')
    
    #cup
    canvas.create_line(250, 200, 250, 500, width=3)
    canvas.create_line(500, 200, 500, 500, width=3)
    #adapted from hw9 https://www.cs.cmu.edu/~112/notes/hw9.html
    canvas.create_arc(250, 525, 500, 475, width=3, style='arc', extent=-180)
    r=50
    canvas.create_oval(app.width*.375-r*2.5, app.height*(1/3)-r*.5, 
                            app.width*.375+r*2.5, app.height*(1/3)+r*.5, width=3)
    
    #pour button
    if app.curIngName != 'None':
        drawButton(canvas, app.kitchen_addBtnDms, 'Add')
    
    drawIngOptions(app, canvas)
    drawSideBar(app, canvas)
    if len(app.madeDrinkDict) != 0:
        drawDrink(app, canvas)
        
    
def drawIngOptions(app, canvas):
    #!ingredients
    #toppings
    canvas.create_image(75, 400, image=ImageTk.PhotoImage(scaleImage(app, app.tapioca, (100,100))))
    canvas.create_image(175, 400, image=ImageTk.PhotoImage(scaleImage(app, app.aloeJelly, (100,100))))
    canvas.create_image(75, 300, image=ImageTk.PhotoImage(scaleImage(app, app.redBean, (100,100))))
    canvas.create_image(175, 300, image=ImageTk.PhotoImage(scaleImage(app, app.pudding, (100,100))))
    
    #ice
    canvas.create_text(115, 25, text='Ice:', font='Arial 20 bold')
    drawButton(canvas, app.kitchen_100iceBtnDms, '100%')
    drawButton(canvas, app.kitchen_75iceBtnDms, '75%')
    drawButton(canvas, app.kitchen_50iceBtnDms, '50%')
    drawButton(canvas, app.kitchen_25iceBtnDms, '25%')
    
    #tea
    canvas.create_image(275, 100, image=ImageTk.PhotoImage(scaleImage(app, app.greenTea, (125, 125))))
    canvas.create_image(375, 100, image=ImageTk.PhotoImage(scaleImage(app, app.blackTea, (115, 115))))
    canvas.create_image(475, 100, image=ImageTk.PhotoImage(scaleImage(app, app.oolongTea, (115, 115))))
    
    #milk
    canvas.create_text(630, 25, text='Milk:', font='Arial 20 bold')
    drawButton(canvas, app.kitchen_wholeMilkBtnDms, 'whole')
    drawButton(canvas, app.kitchen_2pMilkBtnDms, '2%')
    drawButton(canvas, app.kitchen_skimMilkBtnDms, 'skim')
    
    #sugar
    canvas.create_text(630, 200, text='Sugar:', font='Arial 20 bold')
    drawButton(canvas, app.kitchen_100sugarBtnDms, '100%')
    drawButton(canvas, app.kitchen_75sugarBtnDms, '75%')
    drawButton(canvas, app.kitchen_50sugarBtnDms, '50%')
    drawButton(canvas, app.kitchen_25sugarBtnDms, '25%')
    
    #mix and seal
    drawButton(canvas, app.kitchen_mixBtnDms, 'Mix & Seal')
    
def drawSideBar(app, canvas):
    canvas.create_text(875, 25, text='Current Order', font='Arial 20 bold')
    if len(app.curCustDrink) != 0:
        space = 60
        for ing in app.curCustDrink:
            canvas.create_text(875, space, text=ing, font='Arial 20 bold')
            space += 30
        
    canvas.create_text(875, 400, text=f'Current Ingredient:', font='Arial 15 bold')
    canvas.create_text(875, 430, text=f'{app.curIngName}', font='Arial 20 bold')

def drawDrink(app, canvas):
    #cup = 250 by 300
    x0 = 252
    x1 = 499
    y0 = 500
    y1 = 500
    
    for ing in app.madeDrinkList:
        color = getIngColor(app, ing)
        pressLen = app.madeDrinkDict[ing]*25
        #!problem
        if ing == app.madeDrinkList[-1]:
            if app.isPressed:
                y1 = y0
                y0 -= (time.time() - app.startPress)*10
                canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
            # else:
            #     canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
        #!end of problem
        y1 = y0
        y0 -= pressLen
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
        
        # color = getIngColor(app, ing)
        # pressLen = app.madeDrinkDict[ing]*25
        # if ing == app.madeDrinkList[-1]:
        #     if app.isPressed:
        #         y0 -= (time.time() - app.startPress)*10
        #         canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
        #     else:
        #         canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
        # y1 = y0
        # y0 -= pressLen
        # canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
    
    # oldY0, oldY1 = 500, 500
    # for ing in app.madeDrinkList:
    #     # print(app.madeDrinkList)
    #     # print(app.madeDrinkDict)
    #     color = getIngColor(app, ing)
    #     pressLen = app.madeDrinkDict[ing]*25
    #     y1 = oldY1
        
    #     if ing == app.madeDrinkList[-1]:
            
    #         if app.isPressed:
    #             y0 = oldY0
    #             y0 -= (time.time() - app.startPress)*10
    #             # y0 = oldY0 - (time.time() - app.startPress)*10
    #             oldY0 =y0
    #             canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
    #         else:
    #             y0 = oldY0
    #             # canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
    #             # y0 = oldY0-pressLen
    #             y1 = y0
    #             # y1 = oldY1
    #             canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
    #             oldY1 = y0
    #             oldY0 -= pressLen
    #     else:
    #         # y0 = oldY1-pressLen
            
    #         # canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)

    #         y0 = oldY0-pressLen
    #         y1 = oldY1
    #         canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
    #         oldY1 = y0
    #         oldY0 -= pressLen
        
    #     # oldY1 = y0
    #     # oldY0 = y1
    #     # oldY0 -= pressLen

###################################
#controller
###################################
def kitchenScreen_mouseReleased(app, event):
    x, y = event.x, event.y
    # store button
    if isValidClick(x, y, app.kitchen_storeBtnDms):
        app.mode = 'storeScreen'
    # eval button
    elif isValidClick(x, y, app.kitchen_evalBtnDms):
        app.mode = 'evaluationScreen'
    # red bean button
    elif isValidClick(x, y, (30, 253, 120, 347)) and 'red_bean' not in app.madeDrinkList:
        app.curIngName = 'Red Bean'
        app.curIng = 'red_bean'
        app.madeDrinkDict[app.curIng] = 0
    # tapioca button
    elif isValidClick(x, y, (29, 353, 120, 447)) and 'tapioca' not in app.madeDrinkList:
        app.curIngName = 'Tapioca'
        app.curIng = 'tapioca'
        app.madeDrinkDict[app.curIng] = 0
    # pudding button
    elif isValidClick(x, y, (128, 253, 220, 347)) and 'pudding' not in app.madeDrinkList:
        app.curIngName = 'Pudding'
        app.curIng = 'pudding'
        app.madeDrinkDict[app.curIng] = 0
    # aloe jelly button
    elif isValidClick(x, y, (130, 354, 220, 447)) and 'aloe_jelly' not in app.madeDrinkList:
        app.curIngName = 'Aloe Jelly'
        app.curIng = 'aloe_jelly'
        app.madeDrinkDict[app.curIng] = 0
    # green tea button
    elif isValidClick(x, y, (232, 73, 317, 128)) and 'green_tea' not in app.madeDrinkList:
        app.curIngName = 'Green Tea'
        app.curIng = 'green_tea'
        app.madeDrinkDict[app.curIng] = 0
    # black tea button
    elif isValidClick(x, y, (323, 70, 422, 128)) and 'black_tea' not in app.madeDrinkList:
        app.curIngName = 'Black Tea'
        app.curIng = 'black_tea'
        app.madeDrinkDict[app.curIng] = 0
    # oolong tea button
    elif isValidClick(x, y, (429, 70, 524, 128)) and 'oolong_tea' not in app.madeDrinkList:
        app.curIngName = 'Oolong Tea'
        app.curIng = 'oolong_tea'
        app.madeDrinkDict[app.curIng] = 0
    # whole milk button
    elif isValidClick(x, y, app.kitchen_wholeMilkBtnDms) and 'whole' not in app.madeDrinkList:
        app.curIngName = 'Whole Milk'
        app.curIng = 'whole'
        app.madeDrinkDict[app.curIng] = 0
    # 2% milk button
    elif isValidClick(x, y, app.kitchen_2pMilkBtnDms) and '2%' not in app.madeDrinkList:
        app.curIngName = '2% Milk'
        app.curIng = '2%'
        app.madeDrinkDict[app.curIng] = 0
    # skim milk button
    elif isValidClick(x, y, app.kitchen_skimMilkBtnDms) and 'skim' not in app.madeDrinkList:
        app.curIngName = 'Skim Milk'
        app.curIng = 'skim'
        app.madeDrinkDict[app.curIng] = 0
    # 100% ice button
    elif isValidClick(x, y, app.kitchen_100iceBtnDms) and '100%_ice' not in app.madeDrinkList:
        app.curIngName = 'Ice'
        app.curIng = '100%_ice'
        app.madeDrinkDict[app.curIng] = 0
    # 75% ice button
    elif isValidClick(x, y, app.kitchen_75iceBtnDms) and '75%_ice' not in app.madeDrinkList:
        app.curIngName = 'Ice'
        app.curIng = '75%_ice'
        app.madeDrinkDict[app.curIng] = 0
    # 50% ice button
    elif isValidClick(x, y, app.kitchen_50iceBtnDms) and '50%_ice' not in app.madeDrinkList:
        app.curIngName = 'Ice'
        app.curIng = '50%_ice'
        app.madeDrinkDict[app.curIng] = 0
    # 25% ice button
    elif isValidClick(x, y, app.kitchen_25iceBtnDms) and '25%_ice' not in app.madeDrinkList:
        app.curIngName = 'Ice'
        app.curIng = '25%_ice'
        app.madeDrinkDict[app.curIng] = 0
    # 100% sugar button
    elif isValidClick(x, y, app.kitchen_100sugarBtnDms) and '100%_sugar' not in app.madeDrinkList:
        app.curIngName = 'Liquid Sugar'
        app.curIng = '100%_sugar'
        app.madeDrinkDict[app.curIng] = 0
    # 75% sugar button
    elif isValidClick(x, y, app.kitchen_75sugarBtnDms) and '75%_sugar' not in app.madeDrinkList:
        app.curIngName = 'Liquid Sugar'
        app.curIng = '75%_sugar'
        app.madeDrinkDict[app.curIng] = 0
    # 50% sugar button
    elif isValidClick(x, y, app.kitchen_50sugarBtnDms) and '50%_sugar' not in app.madeDrinkList:
        app.curIngName = 'Liquid Sugar'
        app.curIng = '50%_sugar'
        app.madeDrinkDict[app.curIng] = 0
    # 25% sugar button
    elif isValidClick(x, y, app.kitchen_25sugarBtnDms) and '25%_sugar' not in app.madeDrinkList:
        app.curIngName = 'Liquid Sugar'
        app.curIng = '25%_sugar'
        app.madeDrinkDict[app.curIng] = 0
        
    #getting ing timers
    if app.curIngName != 'None' and isValidClick(x, y, app.kitchen_addBtnDms):
        app.lenOfPress = time.time() - app.startPress
        app.cupFullness += app.lenOfPress
        print(f'cupFullness: {app.cupFullness}')
        app.isPressed = False
        #check if cup full
        if app.cupFullness > 12:
            app.cupFullness -= app.lenOfPress
            app.madeDrinkList.remove(app.curIng)
            # del app.madeDrinkDict[app.curIng]
        else:
            app.madeDrinkDict[app.curIng] = app.madeDrinkDict.get(app.curIng, 0) + app.lenOfPress
            app.curIngName = 'None'
            # print(app.madeDrinkDict)
        
        
def kitchenScreen_mousePressed(app, event):
    x, y, = event.x, event.y
    # add button
    if app.curIngName != 'None' and isValidClick(x, y, app.kitchen_addBtnDms):
        app.isPressed = True
        app.startPress = time.time()
        app.madeDrinkList.append(app.curIng)
    
        
def kitchenScreen_timerFired(app):
    checkIfDayOver(app)
    checkIfGameOver(app)    