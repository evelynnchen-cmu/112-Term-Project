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
    canvas.create_line(400, 250, 400, 550, width=3)
    canvas.create_line(650, 250, 650, 550, width=3)
    canvas.create_line(400, 250, 650, 250, width=3)
    canvas.create_line(400, 550, 650, 550, width=3)
    
    #ingredients
        #teas
    #draw all ings
    for i in range(len(app.ingCs)):
        if app.curIngImg != app.ingImgs[i]:
            canvas.create_image(app.ingCs[i], image=ImageTk.PhotoImage(app.ingImgs[i]))
    
    if app.hasItem:
        canvas.create_image(app.x, app.y, image = ImageTk.PhotoImage(app.curIngImg))
    # if app.isLegal:
    #     print('pouring')
    # else:
    #     print('not pouring')
    print(app.sugarCubeCount, app.iceCubeCount)
    #!to make 3D maybe later
    #adapted from hw9 https://www.cs.cmu.edu/~112/notes/hw9.html
    # canvas.create_arc(250, 525, 500, 475, width=3, style='arc', extent=-180)
    # r=50
    # canvas.create_oval(app.width*.375-r*2.5, app.height*(1/3)-r*.5, 
    #                         app.width*.375+r*2.5, app.height*(1/3)+r*.5, width=3)
    
    # drawIngOptions(app, canvas)
    drawSideBar(app, canvas)
    # if len(app.madeDrinkDict) != 0:
    #     drawDrink(app, canvas)
    # print(app.madeDrinkList)
    # print(app.madeDrinkDict)

def drawSideBar(app, canvas):
    canvas.create_text(875, 20, text='Current Order', font='Arial 20 bold underline')
    if len(app.curCustDrink) != 0:
        space = 50
        for ing in app.curCustDrink:
            canvas.create_text(875, space, text=ing, font='Arial 15 bold')
            space += 30
        
    canvas.create_text(875, 400, text=f'Current Ingredient:', font='Arial 15 bold')
    canvas.create_text(875, 430, text=f'{app.curIngName}', font='Arial 20 bold')

def drawDrink(app, canvas):
    #cup = 250 by 300
    x0 = 400
    x1 = 650
    y0 = 550
    y1 = 550
    
    for ing in app.madeDrinkList:
        color = getIngColor(app, ing)
        pressLen = app.madeDrinkDict[ing]*15
        y1 = y0
        
        if ing == app.madeDrinkList[-1]:
            if app.isPressed:
                #?learned about time module from 
                #?https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
                y0 -= (time.time() - app.startPress)*15
                canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
        
        y0 -= pressLen
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
        
###################################
#controller
###################################
def kitchenScreen_mousePressed(app, event):
    x, y = event.x, event.y
    app.startAdd = 0
    app.lenOfAdd = 0
    #green tea
    if isValidIngClick(app, x, y, app.tapiocaC) and 'tapioca' not in app.madeDrinkDict:
        app.curIng = 'tapioca'
        app.curIngImg = app.tapioca
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.tapiocaC
    elif isValidIngClick(app, x, y, app.aloeJellyC) and 'aloe_jelly' not in app.madeDrinkDict:
        app.curIng = 'aloe_jelly'
        app.curIngImg = app.aloeJelly
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.aloeJellyC
    elif isValidIngClick(app, x, y, app.redBeanC) and 'red_bean' not in app.madeDrinkDict:
        app.curIng = 'red_bean'
        app.curIngImg = app.redBean
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.redBeanC
    elif isValidIngClick(app, x, y, app.puddingC) and 'pudding' not in app.madeDrinkDict:
        app.curIng = 'pudding'
        app.curIngImg = app.pudding
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.puddingC
    elif isValidIngClick(app, x, y, app.sugarCubeC):
        #!fix
        app.curIng = 'sugarCube'
        app.curIngImg = app.sugarCube
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.sugarCubeC
    elif isValidIngClick(app, x, y, app.iceCubeC):
        #!fix
        app.curIng = 'iceCube'
        app.curIngImg = app.iceCube
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.iceCubeC
    elif isValidIngClick(app, x, y, app.wholeMilkC) and 'whole_milk' not in app.madeDrinkDict:
        app.curIng = 'whole_milk'
        app.curIngImg = app.wholeMilk
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.wholeMilkC
    elif isValidIngClick(app, x, y, app.twoPMilkC) and '2%_milk' not in app.madeDrinkDict:
        app.curIng = '2%_milk'
        app.curIngImg = app.twoPMilk
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.twoPMilkC
    elif isValidIngClick(app, x, y, app.skimMilkC) and 'skim_milk' not in app.madeDrinkDict:
        app.curIng = 'skim_milk'
        app.curIngImg = app.skimMilk
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.skimMilkC
    elif isValidIngClick(app, x, y, app.greenTeaC) and 'green_tea' not in app.madeDrinkDict:
        app.curIng = 'green_tea'
        app.curIngImg = app.greenTea
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.greenTeaC
    elif isValidIngClick(app, x, y, app.blackTeaC) and 'black_tea' not in app.madeDrinkDict:
        app.curIng = 'black_tea'
        app.curIngImg = app.blackTea
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.blackTeaC
    elif isValidIngClick(app, x, y, app.oolongTeaC) and 'oolong_tea' not in app.madeDrinkDict:
        app.curIng = 'oolong_tea'
        app.curIngImg = app.oolongTea
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.oolongTeaC
    # print(app.curIng)
        
def kitchenScreen_mouseReleased(app, event):
    if app.hasItem and app.isLegal:
        app.lenOfAdd = time.time() - app.startAdd
        app.cupFullness += app.lenOfAdd
        app.madeDrinkList.append(app.curIng)
        app.madeDrinkDict[app.curIng] = app.madeDrinkDict.get(app.curIng, 0) + app.lenOfAdd
    
    
    if app.curIng != 'sugarCube' and app.curIng != 'iceCube' and app.curIng != '':    
        if app.madeDrinkDict[app.curIng] == 0:
            del app.madeDrinkDict[app.curIng]
    
    app.itemAtRest = True
    app.hasItem = False
    app.isLegal = False
    app.curIngImg = ''
    
    app.x = 0
    app.y = 0
    
    
    
def kitchenScreen_mouseDragged(app, event):
    if app.hasItem:
        app.x, app.y, = event.x, event.y
    
    #if item is above cup
    if 425 < app.x < 625 and 0 < app.y < 250:
        
        if app.startAdd == 0:
            app.startAdd = time.time()
        app.isLegal = True
    else:
        app.isLegal = False
    
    if app.hasItem and app.isLegal:
        if app.curIng == 'sugarCube':
            app.sugarCubeCount += 1
            app.hasItem = False
            # app.itemAtRest = True
        elif app.curIng == 'iceCube':
            app.iceCubeCount += 1
            app.hasItem = False
        else:
            app.madeDrinkDict[app.curIng] = app.madeDrinkDict.get(app.curIng, 0) + app.lenOfAdd
        
        

# def kitchenScreen_mouseReleased(app, event):
#     x, y = event.x, event.y
#     # store button
#     if isValidClick(x, y, app.kitchen_storeBtnDms):
#         app.mode = 'storeScreen'
#     # eval button
#     elif isValidClick(x, y, app.kitchen_evalBtnDms):
#         evaluateDrink(app)
#         app.evalRevealTimer = 0
#         app.mode = 'evaluationScreen'
        
#     # red bean button
#     elif isValidClick(x, y, (30, 253, 120, 347)) and 'red_bean' not in app.madeDrinkList:
#         app.curIngName = 'Red Bean'
#         app.curIng = 'red_bean'
#         app.madeDrinkDict[app.curIng] = 0
#     # tapioca button
#     elif isValidClick(x, y, (29, 353, 120, 447)) and 'tapioca' not in app.madeDrinkList:
#         app.curIngName = 'Tapioca'
#         app.curIng = 'tapioca'
#         app.madeDrinkDict[app.curIng] = 0
#     # pudding button
#     elif isValidClick(x, y, (128, 253, 220, 347)) and 'pudding' not in app.madeDrinkList:
#         app.curIngName = 'Pudding'
#         app.curIng = 'pudding'
#         app.madeDrinkDict[app.curIng] = 0
#     # aloe jelly button
#     elif isValidClick(x, y, (130, 354, 220, 447)) and 'aloe_jelly' not in app.madeDrinkList:
#         app.curIngName = 'Aloe Jelly'
#         app.curIng = 'aloe_jelly'
#         app.madeDrinkDict[app.curIng] = 0
#     # green tea button
#     elif isValidClick(x, y, (232, 73, 317, 128)) and 'green_tea' not in app.madeDrinkList:
#         app.curIngName = 'Green Tea'
#         app.curIng = 'green_tea'
#         app.madeDrinkDict[app.curIng] = 0
#     # black tea button
#     elif isValidClick(x, y, (323, 70, 422, 128)) and 'black_tea' not in app.madeDrinkList:
#         app.curIngName = 'Black Tea'
#         app.curIng = 'black_tea'
#         app.madeDrinkDict[app.curIng] = 0
#     # oolong tea button
#     elif isValidClick(x, y, (429, 70, 524, 128)) and 'oolong_tea' not in app.madeDrinkList:
#         app.curIngName = 'Oolong Tea'
#         app.curIng = 'oolong_tea'
#         app.madeDrinkDict[app.curIng] = 0
#     # whole milk button
#     elif isValidClick(x, y, app.kitchen_wholeMilkBtnDms) and 'whole' not in app.madeDrinkList:
#         app.curIngName = 'Whole Milk'
#         app.curIng = 'whole'
#         app.madeDrinkDict[app.curIng] = 0
#     # 2% milk button
#     elif isValidClick(x, y, app.kitchen_2pMilkBtnDms) and '2%' not in app.madeDrinkList:
#         app.curIngName = '2% Milk'
#         app.curIng = '2%'
#         app.madeDrinkDict[app.curIng] = 0
#     # skim milk button
#     elif isValidClick(x, y, app.kitchen_skimMilkBtnDms) and 'skim' not in app.madeDrinkList:
#         app.curIngName = 'Skim Milk'
#         app.curIng = 'skim'
#         app.madeDrinkDict[app.curIng] = 0
#     # 100% ice button
#     elif isValidClick(x, y, app.kitchen_100iceBtnDms) and '100%_ice' not in app.madeDrinkList:
#         app.curIngName = 'Ice'
#         app.curIng = '100%_ice'
#         app.madeDrinkDict[app.curIng] = 0
#     # 75% ice button
#     elif isValidClick(x, y, app.kitchen_75iceBtnDms) and '75%_ice' not in app.madeDrinkList:
#         app.curIngName = 'Ice'
#         app.curIng = '75%_ice'
#         app.madeDrinkDict[app.curIng] = 0
#     # 50% ice button
#     elif isValidClick(x, y, app.kitchen_50iceBtnDms) and '50%_ice' not in app.madeDrinkList:
#         app.curIngName = 'Ice'
#         app.curIng = '50%_ice'
#         app.madeDrinkDict[app.curIng] = 0
#     # 25% ice button
#     elif isValidClick(x, y, app.kitchen_25iceBtnDms) and '25%_ice' not in app.madeDrinkList:
#         app.curIngName = 'Ice'
#         app.curIng = '25%_ice'
#         app.madeDrinkDict[app.curIng] = 0
#     # 100% sugar button
#     elif isValidClick(x, y, app.kitchen_100sugarBtnDms) and '100%_sugar' not in app.madeDrinkList:
#         app.curIngName = 'Liquid Sugar'
#         app.curIng = '100%_sugar'
#         app.madeDrinkDict[app.curIng] = 0
#     # 75% sugar button
#     elif isValidClick(x, y, app.kitchen_75sugarBtnDms) and '75%_sugar' not in app.madeDrinkList:
#         app.curIngName = 'Liquid Sugar'
#         app.curIng = '75%_sugar'
#         app.madeDrinkDict[app.curIng] = 0
#     # 50% sugar button
#     elif isValidClick(x, y, app.kitchen_50sugarBtnDms) and '50%_sugar' not in app.madeDrinkList:
#         app.curIngName = 'Liquid Sugar'
#         app.curIng = '50%_sugar'
#         app.madeDrinkDict[app.curIng] = 0
#     # 25% sugar button
#     elif isValidClick(x, y, app.kitchen_25sugarBtnDms) and '25%_sugar' not in app.madeDrinkList:
#         app.curIngName = 'Liquid Sugar'
#         app.curIng = '25%_sugar'
#         app.madeDrinkDict[app.curIng] = 0
        
#     #getting ing timers
#     if app.curIngName != 'None' and isValidClick(x, y, app.kitchen_addBtnDms):
#         app.lenOfPress = time.time() - app.startPress
#         app.cupFullness += app.lenOfPress
#         print(f'cupFullness: {app.cupFullness}')
#         app.isPressed = False
#         #check if cup full
#         if app.cupFullness > 20:
#             app.cupFullness -= app.lenOfPress
#             app.madeDrinkList.remove(app.curIng)
#             # del app.madeDrinkDict[app.curIng]
#         else:
#             app.madeDrinkDict[app.curIng] = app.madeDrinkDict.get(app.curIng, 0) + app.lenOfPress
#             app.curIngName = 'None'
#             print(app.madeDrinkDict)
        
        
# def kitchenScreen_mousePressed(app, event):
#     x, y, = event.x, event.y
#     # add button
#     if app.curIngName != 'None' and isValidClick(x, y, app.kitchen_addBtnDms):
#         app.isPressed = True
#         app.startPress = time.time()
#         app.madeDrinkList.append(app.curIng)
    
        
def kitchenScreen_timerFired(app):
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    app.currentDay.canNextCust(app)
    checkIfGameOver(app)    