from classes import *

###################################
#view
###################################
def kitchenScreen_redrawAll(app, canvas):
    #blue sidebar
    canvas.create_rectangle(750, 0, app.width, app.height, fill='lightblue1', width=0)
    
    #background 
    canvas.create_rectangle(0, 0, 750, app.height, fill='#D3D3D3', width=0)
    
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, fill='black', width=3)
        
    # drawButton(canvas, app.kitchen_storeBtnDms, 'Store')
    if app.isMixed:
        drawButton(canvas, app.kitchen_evalBtnDms, 'Evaluate')
    
    if not app.isMixed:
        drawButton(canvas, app.kitchen_mixBtnDms, 'Mix')
    drawSideBar(app, canvas)
    print(app.madeDrinkDict)
    # print(app.madeDrinkList)
    
    if app.isMixed:
        
        x0 = 251
        x1 = 501
        y0 = 549
        y1 = 549
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
            addLen = mixedDrinkToppings[ing]*15
            y1 = y0 
            y0 -= addLen
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
        #draw mixed liquid
        canvas.create_rectangle(x0, 549-(app.cupFullness*15), x1, 
                                549-(topOfToppings*15), fill=newColor, width=0)
        
        drawCubes(canvas, app.iceCubeCount, 251)
        canvas.create_image(376, 404, image=ImageTk.PhotoImage(app.cupOutlineGray))
    else:
        
        #ingredients
        #draw all ings
        for i in range(len(app.ingCs)):
            if app.curIngImg != app.ingImgs[i]:
                canvas.create_image(app.ingCs[i], image=ImageTk.PhotoImage(app.ingImgs[i]))

        if app.hasItem:
            canvas.create_image(app.x, app.y, image = ImageTk.PhotoImage(app.curIngImg))

        if len(app.madeDrinkDict) != 0:
            drawDrink(app, canvas)
        if app.iceCubeCount + app.sugarCubeCount != 0:
            drawCubes(canvas, (app.iceCubeCount + app.sugarCubeCount), 410)
        canvas.create_image(526, 404, image=ImageTk.PhotoImage(app.cupOutlineGray))

def drawCubes(canvas, numOfSquares, x):
    #!optimize this
    canvas.create_line(410, 500, 527, 500, fill='red', width=10)
    for i in range(numOfSquares):
        if i >= 19:
            canvas.create_rectangle(x+(62.5*(i-20)), 248, x+(62.5*((i+1)-20)), 299, width=2)
        elif i >= 15:
            canvas.create_rectangle(x+(62.5*(i-16)), 298, x+(62.5*((i+1)-16)), 349, width=2)
        elif i >= 11:
            canvas.create_rectangle(x+(62.5*(i-12)), 348, x+(62.5*((i+1)-12)), 399, width=2)
        elif i >= 7:
            canvas.create_rectangle(x+(62.5*(i-8)), 398, x+(62.5*((i+1)-8)), 449, width=2)
        elif i >= 3:
            canvas.create_rectangle(x+(62.5*(i-4)), 448, x+(62.5*((i+1)-4)), 499, width=2)
        elif i < 3:
            canvas.create_rectangle(x+(62.5*(i)), 498, x+(62.5*(i+1)), 549, width=2)
            
def drawSideBar(app, canvas):
    canvas.create_rectangle(775, 25, 975, 250, fill='#eecf90', width=3)
    canvas.create_text(875, 40, text=f"Customer #{(app.currentDay.custIndex)}", font='Courier 20 bold')    
    if len(app.curCustDrink) != 0:
        space = 70
        for ing in app.curCustDrink:
            canvas.create_text(875, space, text=ing, font='Courier 15 bold')
            space += 30

def drawDrink(app, canvas):
    #cup = 250 by 300
    x0 = 401
    x1 = 649
    y0 = 550
    y1 = 550
    
    for ing in app.madeDrinkList:
        color = getIngColor(app, ing)
        addLen = app.madeDrinkDict[ing]*15
        y1 = y0
        
        if ing == app.madeDrinkList[-1]:
            if app.isAdding:
                #?learned about time module from 
                #?https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
                y0 -= (time.time() - app.startAdd)*15
                canvas.create_rectangle(app.x-15, app.y+app.ingR, app.x+15, y0, fill=color, width=0)
                canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)
        
        y0 -= addLen
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
        app.curIng = 'sugarCube'
        app.curIngImg = app.sugarCube
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.sugarCubeC
    elif isValidIngClick(app, x, y, app.iceCubeC):
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
    x, y, = event.x, event.y
    
    #mix button
    if isValidClick(x, y, app.kitchen_mixBtnDms):
        app.isMixed = True
    #store button
    # elif isValidClick(x, y, app.kitchen_storeBtnDms):
    #     app.mode = 'storeScreen'
    # eval button
    elif isValidClick(x, y, app.kitchen_evalBtnDms):
        print('hi')
        evaluateDrink(app)
        # app.evalRevealTimer = 0
        app.mode = 'evaluationScreen'
    
    if app.hasItem and app.isLegal:
        app.lenOfAdd = time.time() - app.startAdd
        app.cupFullness += app.lenOfAdd
        app.madeDrinkDict[app.curIng] = app.madeDrinkDict.get(app.curIng, 0) + app.lenOfAdd
    
    #!idk
    # if app.curIng != 'sugarCube' and app.curIng != 'iceCube' and app.curIng != '':    
    #     #!bug
    #     if app.madeDrinkDict[app.curIng] == 0:
    #         del app.madeDrinkDict[app.curIng]
    #         app.madeDrinkList.pop()
    
    app.itemAtRest = True
    app.hasItem = False
    app.isLegal = False
    app.curIngImg = ''
    app.isAdding = False
    app.entered = False
    
    app.x = 0
    app.y = 0
    
def kitchenScreen_mouseDragged(app, event):
    if app.hasItem:
        if event.x < 750:
            app.x, app.y, = event.x, event.y
    
    #if item is above cup
    if app.curIng != 'iceCube' and app.curIng != 'sugarCube':
        if 425 < app.x < 625 and 0 < app.y < 250:
            app.entered = True
            app.isAdding = True
            if app.startAdd == 0:
                app.startAdd = time.time()
            app.isLegal = True
        else:
            app.isLegal = False 
            app.isAdding = False
            if app.entered:
                app.hasItem = False

        if app.hasItem and app.isLegal:
            app.madeDrinkDict[app.curIng] = app.madeDrinkDict.get(app.curIng, 0) + app.lenOfAdd
            if app.curIng not in app.madeDrinkList:
                app.madeDrinkList.append(app.curIng)
    else:
        if app.sugarCubeCount + app.iceCubeCount < 23:
            if app.curIng == 'sugarCube':
                app.sugarCubeCount += 1
                app.hasItem = False
                app.curIng = ''
            elif app.curIng == 'iceCube':
                app.iceCubeCount += 1
                app.hasItem = False
                app.curIng = ''
                
def kitchenScreen_timerFired(app):
    app.currentDay.canNextCust(app)
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    
    checkIfGameOver(app) 

    
    
