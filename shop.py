from classes import *

###################################
#view
###################################
def shopScreen_redrawAll(app, canvas):
    
    #put in main these below
    tipsJarSmall = scaleImage(app, app.tipsJar, (100, 100))
        
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                fill='black', width=3)
        
    #horizontal divider
    canvas.create_line(0, app.height/10, app.width*(3/4), app.height/10, 
                                                fill='black', width=3)
    #day
    drawDayProgBar(app, canvas)
    #money
    canvas.create_text(600, 30, text=f'Money: ${app.money}', font='Arial 25 bold')
        
    #counter
    canvas.create_line(0, app.height*(5/6), app.width*(3/4), app.height*(5/6), fill='black', width=3)
    canvas.create_rectangle(0, app.height*(2/3), app.width*(3/4), app.height, fill='bisque2')
        
    #cash register
    canvas.create_rectangle(25, 325, 125, 385, fill='black')
    canvas.create_rectangle(62.5, 375, 87.5, 400, fill='black')
    canvas.create_text(75, 355, text='$$$', fill='green', font='Arial 15 bold')

    #tips jar
    canvas.create_image(650, 350, 
            image=ImageTk.PhotoImage(tipsJarSmall))
        
    drawButton(canvas, app.shop_takeOrderBtnDms, 'Take Order')
    drawButton(canvas, app.shop_kitchenBtnDms, 'Kitchen')
    drawButton(canvas, app.shop_storeBtnDms, 'Store')

###################################    
#controller
###################################
def shopScreen_mouseReleased(app, event):
    # kitchen button
    if isValidClick(event.x, event.y, app.shop_kitchenBtnDms):
        app.mode = 'kitchenScreen'
    # store button
    elif isValidClick(event.x, event.y, app.shop_storeBtnDms):
        app.mode = 'storeScreen'
        
def shopScreen_timerFired(app):
    checkIfDayOver(app)
    checkIfGameOver(app)
    
        