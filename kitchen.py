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
    canvas.create_line(app.width*.25, app.height*(1/3), app.width*.25, app.height*(5/6), width=3)
    canvas.create_line(app.width*.5, app.height*(1/3), app.width*.5, app.height*(5/6), width=3)
    #adapted from hw9 https://www.cs.cmu.edu/~112/notes/hw9.html
    canvas.create_arc(app.width*.25, app.height*(4/6)+125, 
                        app.width*.5, app.height*(4/6)+75, width=3, style='arc', extent=-180)
    r=app.width*.05
    canvas.create_oval(app.width*.375-r*2.5, app.height*(1/3)-r*.5, 
                            app.width*.375+r*2.5, app.height*(1/3)+r*.5, width=3)
    
    drawIngs(app, canvas)
    
    
def drawIngs(app, canvas):
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
    
    #toppings rectangles
    # canvas.create_rectangle(30, 253, 120, 347, width=3)
    # canvas.create_rectangle(29, 353, 120, 447, width=3)
    # canvas.create_rectangle(128, 253, 220, 347, width=3)
    # canvas.create_rectangle(130, 354, 220, 447, width=3)
    
    #tea rectangles
    # canvas.create_rectangle(232, 73, 317, 128, width=3)
    # canvas.create_rectangle(323, 70, 422, 128, width=3)
    # canvas.create_rectangle(429, 70, 524, 128, width=3)
    
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
    elif isValidClick(x, y, (30, 253, 120, 347)):
        app.curIng = 'red_bean'
    # tapioca button
    elif isValidClick(x, y, (29, 353, 120, 447)):
        app.curIng = 'tapioca'
    # pudding button
    elif isValidClick(x, y, (128, 253, 220, 347)):
        app.curIng = 'pudding'
    # aloe jelly button
    elif isValidClick(x, y, (130, 354, 220, 447)):
        app.curIng = 'aloe_jelly'
    # green tea button
    elif isValidClick(x, y, (232, 73, 317, 128)):
        app.curIng = 'green_tea'
    # black tea button
    elif isValidClick(x, y, (323, 70, 422, 128)):
        app.curIng = 'black_tea'
    # oolong tea button
    elif isValidClick(x, y, (429, 70, 524, 128)):
        app.curIng = 'oolong_tea'
    # whole milk button
    elif isValidClick(x, y, app.kitchen_wholeMilkBtnDms):
        app.curIng = 'whole'
    # 2% milk button
    elif isValidClick(x, y, app.kitchen_2pMilkBtnDms):
        app.curIng = '2%'
    # skim milk button
    elif isValidClick(x, y, app.kitchen_skimMilkBtnDms):
        app.curIng = 'skim'
    # 100% ice button
    elif isValidClick(x, y, app.kitchen_100iceBtnDms):
        app.curIng = '100%_ice'
    # 75% ice button
    elif isValidClick(x, y, app.kitchen_75iceBtnDms):
        app.curIng = '75%_ice'
    # 50% ice button
    elif isValidClick(x, y, app.kitchen_50iceBtnDms):
        app.curIng = '50%_ice'
    # 25% ice button
    elif isValidClick(x, y, app.kitchen_25iceBtnDms):
        app.curIng = '25%_ice'
    # 100% sugar button
    elif isValidClick(x, y, app.kitchen_100sugarBtnDms):
        app.curIng = '100%_sugar'
    # 75% sugar button
    elif isValidClick(x, y, app.kitchen_75sugarBtnDms):
        app.curIng = '75%_sugar'
    # 50% sugar button
    elif isValidClick(x, y, app.kitchen_50sugarBtnDms):
        app.curIng = '50%_sugar'
    # 25% sugar button
    elif isValidClick(x, y, app.kitchen_25sugarBtnDms):
        app.curIng = '25%_sugar'
    
    print(app.curIng)
        
def kitchenScreen_timerFired(app):
    checkIfDayOver(app)
    checkIfGameOver(app)
    
    
        