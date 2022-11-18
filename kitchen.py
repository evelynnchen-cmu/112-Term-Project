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
    #copied from hw9 https://www.cs.cmu.edu/~112/notes/hw9.html
    canvas.create_arc(app.width*.25, app.height*(4/6)+125, 
                        app.width*.5, app.height*(4/6)+75, width=3, style='arc', extent=-180)
    r=app.width*.05
    canvas.create_oval(app.width*.375-r*2.5, app.height*(1/3)-r*.5, 
                            app.width*.375+r*2.5, app.height*(1/3)+r*.5, width=3)
    
    #!ingredients
    #toppings
    canvas.create_image(75, 450, image=ImageTk.PhotoImage(scaleImage(app, app.tapioca, (100,100))))
    canvas.create_image(175, 450, image=ImageTk.PhotoImage(scaleImage(app, app.aloeJelly, (100,100))))
    canvas.create_image(75, 350, image=ImageTk.PhotoImage(scaleImage(app, app.redBean, (100,100))))
    canvas.create_image(175, 350, image=ImageTk.PhotoImage(scaleImage(app, app.pudding, (100,100))))
    
    #ice
    canvas.create_text(115, 25, text='Ice:', font='Arial 20 bold')
    drawButton(canvas, app.kitchen_100iceBtnDms, '100% ice')
    drawButton(canvas, app.kitchen_75iceBtnDms, '75% ice')
    drawButton(canvas, app.kitchen_50iceBtnDms, '50% ice')
    drawButton(canvas, app.kitchen_25iceBtnDms, '25% ice')
    
    #tea
    canvas.create_image(275, 100, image=ImageTk.PhotoImage(scaleImage(app, app.greenTea, (125, 125))))
    canvas.create_image(375, 100, image=ImageTk.PhotoImage(scaleImage(app, app.blackTea, (115, 115))))
    canvas.create_image(475, 100, image=ImageTk.PhotoImage(scaleImage(app, app.oolongTea, (115, 115))))
    
    #milk
    canvas.create_text(630, 25, text='Milk:', font='Arial 20 bold')
    drawButton(canvas, app.kitchen_wholeMilkBtnDms, 'whole')
    drawButton(canvas, app.kitchen_2pMilkBtnDms, '2%')
    drawButton(canvas, app.kitchen_skimMilkBtnDms, 'skim')
    
    
    
    
    
    
    
###################################
#controller
###################################
def kitchenScreen_mouseReleased(app, event):
    # store button
    if isValidClick(event.x, event.y, app.kitchen_storeBtnDms):
        app.mode = 'storeScreen'
    # eval button
    elif isValidClick(event.x, event.y, app.kitchen_evalBtnDms):
        app.mode = 'evaluationScreen'
        
def kitchenScreen_timerFired(app):
    checkIfGameOver(app)
    checkIfDayOver(app)
    
        