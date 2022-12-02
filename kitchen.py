from classes import *

###################################
#view
###################################
def kitchenScreen_redrawAll(app, canvas):
    #draws kitchen layout
    drawBckg(app, canvas)
    #draws customer's order ticket
    drawSideBar(app, canvas)
    #draws customer's ongoing wait time
    drawCurCustWaitTime(app, canvas)
    #notifies user if a new customer arrived
    drawIfNewCust(app, canvas)
    #helps user know where to add to drink
    drawPourGuide(app, canvas)
    
    #checks if the user wants to be done with the drink and mix it
    if app.isMixed:
        drawMixedDrinkMiniScreen(app, canvas)
    else:
        drawDrinkAssembly(app, canvas)

def drawBckg(app, canvas):
    #background 
    canvas.create_rectangle(0, 0, 750, app.height, fill='#D3D3D3', width=0)
    
    #blue sidebar
    canvas.create_rectangle(750, 0, app.width, app.height, fill='lightblue1', width=0)
    
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, fill='black', width=3)

def drawSideBar(app, canvas):
    #yellow ticket
    canvas.create_rectangle(775, 25, 975, 250, fill='#eecf90', width=3)
    canvas.create_text(875, 40, text=f"Customer #{(app.currentDay.custIndex)}", 
                       font='Courier 20 bold')    
    if len(app.curCustDrink) != 0:
        space = 70
        for ing in app.curCustDrink:
            canvas.create_text(875, space, text=ing, font='Courier 15 bold')
            space += 30

def drawCurCustWaitTime(app, canvas):
    canvas.create_rectangle(775, 280, 975, 360, fill='MediumPurple1', width=3)
    canvas.create_text(875, 295, text='Time Since', font='Courier 15 bold')
    canvas.create_text(875, 320, text=f'Customer Arrived:', font='Courier 14 bold')
    canvas.create_text(875, 345, text=f'{app.currentDay.custList[app.currentDay.custIndex-1].waitTime/10}',
                       font='Courier 15 bold')

def drawIfNewCust(app, canvas):
    if app.isThereCust and not app.isMixed:
        canvas.create_rectangle(15, 15, 150, 55, fill='coral1', width=2)
        canvas.create_text(82.5, 27.5, text='New Customer', font='Courier 10 bold')
        canvas.create_text(82.5, 42.5, text='Waiting', font='Courier 10 bold')

def drawPourGuide(app, canvas):
    if app.hasItem:
        canvas.create_rectangle(400, 50, 650, 250, fill='coral1', width=2)
        canvas.create_text(525, 150, text='Drag in here', font='Courier 13 bold')
        canvas.create_text(525, 165, text='to add', font='Courier 13 bold')

def drawMixedDrinkMiniScreen(app, canvas):
    #evaluate button display
    drawButton(canvas, app.kitchen_evalBtnDms, 'Evaluate')
    
    x0 = 251
    x1 = 501
    y0 = 549
    y1 = 549
    newColor = mixDrink(app)
    mixedDrinkToppings = dict()
    topOfToppings = 0
    
    for ing in app.madeDrinkDict:
        #get dict of the drink's toppings
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
    
    if app.iceCubeCount > 0:
        drawIceCubes(app, canvas, 300)
        
    #cup
    canvas.create_image(376, 403, image=ImageTk.PhotoImage(app.cupOutlineGray))

def drawDrinkAssembly(app, canvas):
    #mix button display
    drawButton(canvas, app.kitchen_mixBtnDms, 'Mix')

    #draw all ingredient options
    for i in range(len(app.ings)):
        if app.curIng != app.ings[i]:
            canvas.create_image(app.ingCs[i], image=ImageTk.PhotoImage(app.ingImgs[i]))

    if app.hasItem:
        canvas.create_image(app.x, app.y, image = ImageTk.PhotoImage(app.curIngImg))

    #drink liquid
    if len(app.madeDrinkDict) != 0:
        drawDrink(app, canvas)
    
    #ice cubes
    if app.iceCubeCount > 0:
        drawIceCubes(app, canvas, 445)
        
    #sugar cubes
    if app.sugarCubeCount > 0:
        drawSugarCubes(app, canvas)

    #cup
    canvas.create_image(526, 404, image=ImageTk.PhotoImage(app.cupOutlineGray))
    
    if app.neededAccuracy <= 80:
        #recommended fill lines
        #toppings
        canvas.create_rectangle(630, 489, 650, 491, fill='black')
        canvas.create_text(690, 490, text='Topping', font='Courier 10 bold')
        
        #milk
        canvas.create_rectangle(635, 443, 655, 445, fill='black')
        canvas.create_text(680, 444, text='Milk', font='Courier 10 bold')

def drawDrink(app, canvas):
    x0 = 401
    x1 = 649
    y0 = 550
    y1 = 550
    
    for ing in app.madeDrinkList:
        color = getIngColor(app, ing)
        addLen = app.madeDrinkDict[ing]*15
        y1 = y0
        
        if ing == app.madeDrinkList[-1] and app.hasItem:
            #draws the drink filling up in real time
            if app.isAdding:
                #?learned about time module from 
                #?https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
                y0 -= (time.time() - app.startAdd)*15
                
                #draw pouring rectangle
                if ing in app.teaOPTIONS:
                    canvas.create_rectangle(app.x-35, app.y+30, app.x-25, y0, fill=color, width=0)
                elif ing in app.milkOPTIONS:
                    canvas.create_rectangle(app.x-35, app.y+10, app.x-25, y0, fill=color, width=0)
                elif ing in app.toppingsOPTIONS:
                    canvas.create_rectangle(app.x-40, app.y+30, app.x-25, y0, fill=color, width=0)
                    
                    #random breaks in topping
                    if app.y < app.randomSpot < y0-10:
                        canvas.create_rectangle(app.x-40, app.randomSpot, app.x-25, 20+app.randomSpot, fill='#D3D3D3', width=0)
                    
                canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)

        y0 -= addLen
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)

def drawIceCubes(app, canvas, x):
    topOfDrink = 0
    #getting the current top of the drink
    for ing in app.madeDrinkDict:
        topOfDrink += app.madeDrinkDict[ing]

    if len(app.madeDrinkList) != 0:
        #draws ice cube(s) depending on what is in the drink
        if app.madeDrinkList[-1] in app.teaOPTIONS or app.madeDrinkList[-1] in app.milkOPTIONS:
            #ice cube(s) will sit under liquid
            if 549-(topOfDrink*15) < 514:
                for i in range(app.iceCubeCount):
                    canvas.create_rectangle(x+(35*i), 549-(topOfDrink*15), 
                                            x+(35*(i+1)), 549-((topOfDrink*15)-35), 
                                            width=0.5, fill='#C6DCF5')
            else:
                for i in range(app.iceCubeCount):
                    canvas.create_rectangle(x+(35*i), 513, x+(35*(i+1)), 549, 
                                            width=0.5, fill='#C6DCF5')
        elif app.madeDrinkList[-1] in app.toppingsOPTIONS:
            #ice cube(s) will sit on top of toppings
            if 549-(topOfDrink*15) > 252:
                for i in range(app.iceCubeCount):
                    canvas.create_rectangle(x+(35*i), 549-(topOfDrink*15)-35, 
                        x+(35*(i+1)), 549-(topOfDrink*15), width=0.5, 
                                            fill='#C6DCF5')
            else:
                for i in range(app.iceCubeCount):
                    canvas.create_rectangle(x+(35*i), 513, x+(35*(i+1)), 549, 
                                            width=0.5, fill='#C6DCF5')
    else:
        #ice cube(s) will sit at the bottom of the cup
        for i in range(app.iceCubeCount):
                canvas.create_rectangle(x+(35*i), 513, x+(35*(i+1)), 549, 
                                        width=0.5, fill='#C6DCF5')
 
def drawSugarCubes(app, canvas):
    for i in range(app.sugarCubeCount):
        canvas.create_rectangle(445+(25*i), 549-(app.sugarY*15)-25, 
                            445+(25*(i+1)), 549-(app.sugarY*15), width=0.5, 
                            fill='#FAF9F6') 
  
###################################
#controller
###################################
def kitchenScreen_mousePressed(app, event):
    x, y = event.x, event.y
    app.startAdd = 0
    app.lenOfAdd = 0
    
    #checks what ingredient the user clicked on
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
    elif (isValidIngClick(app, x, y, app.lycheeJellyC) and 'lychee_jelly' 
          not in app.madeDrinkDict and 'lychee_jelly' in app.toppingsOPTIONS):
        app.curIng = 'lychee_jelly'
        app.curIngImg = app.lycheeJelly
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.lycheeJellyC
    elif (isValidIngClick(app, x, y, app.mangoJellyC) and 'mango_jelly' 
          not in app.madeDrinkDict and 'mango_jelly' in app.toppingsOPTIONS):
        app.curIng = 'mango_jelly'
        app.curIngImg = app.mangoJelly
        app.hasItem = True
        app.itemAtRest = False
        app.x, app.y = app.mangoJellyC
        
def kitchenScreen_mouseReleased(app, event):
    x, y, = event.x, event.y
    
    #mix button check
    if isValidClick(x, y, app.kitchen_mixBtnDms):
        app.isMixed = True
    elif isValidClick(x, y, app.kitchen_evalBtnDms):
        evaluateDrink(app)
        app.mode = 'evaluationScreen'
    
    #stops adding ingredient to the drink and records its time
    if app.hasItem and app.isLegal:
        app.lenOfAdd = time.time() - app.startAdd
        #checks if cup overflowed
        if app.cupFullness+app.lenOfAdd <= 20:
            app.cupFullness += app.lenOfAdd
            app.madeDrinkDict[app.curIng] = (app.madeDrinkDict.get(app.curIng, 0) 
                                            + app.lenOfAdd)
    
    #resets dragging/pouring variables
    app.itemAtRest = True
    app.hasItem = False
    app.isLegal = False
    app.curIng = ''
    app.curIngImg = ''
    app.isAdding = False
    app.entered = False
    app.isRotated = False

#?learned about mouseDragged from 
#?https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#events    
def kitchenScreen_mouseDragged(app, event):
    #keeps ingredient in building space
    if app.hasItem:
        if event.x < 750:
            app.x, app.y, = event.x, event.y
    
    if app.curIng != 'iceCube' and app.curIng != 'sugarCube':
        #if ingredient is above cup
        if 437 < app.x < 675 and 50 < app.y < 250:
            app.isLegal = True
            app.entered = True
            app.isAdding = True
            
            #simulates pouring motion
            if not app.isRotated:
                #?.rotate idea from Pat Virtue via Piazza and gave reference of 
                #?https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.rotate
                if app.curIngImg != '':
                    app.curIngImg = app.curIngImg.rotate(angle=90)
                app.isRotated = True
        
            if app.startAdd == 0:
                app.startAdd = time.time()
        else:
            app.isLegal = False 
            app.isAdding = False
            app.isRotated = False
            if app.entered:
                app.hasItem = False

        #adds ingredient to made drink dictionary and list
        if app.hasItem and app.isLegal:
            app.madeDrinkDict[app.curIng] = (app.madeDrinkDict.get(app.curIng, 0) 
                                             + app.lenOfAdd)
            if app.curIng not in app.madeDrinkList:
                app.madeDrinkList.append(app.curIng)
    else:
        #adding sugar/ice cube(s)
        if 425 < app.x < 650 and 50 < app.y < 250:
            if app.curIng == 'sugarCube':
                if app.sugarCubeCount < 4:
                    app.sugarCubeCount += 1
                    #get where the sugar cubes land in the drink
                    if app.sugarCubeCount == 1:
                        for ing in app.madeDrinkDict:
                            app.sugarY += app.madeDrinkDict[ing]
                    app.curIng = ''
                    app.hasItem = False
                    
            if app.curIng == 'iceCube':
                if app.iceCubeCount < 4:
                    app.iceCubeCount += 1
                    app.curIng = ''
                    app.hasItem = False
                    
                
def kitchenScreen_timerFired(app):
    
    # print(app.madeDrinkList)
    # print(app.madeDrinkDict)
    app.randomSpot = random.randint(250, 550)
    app.currentDay.canNextCust(app)
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    
    checkIfGameOver(app) 