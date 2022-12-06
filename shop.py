from classes import *

###################################
#view
###################################
def shopScreen_redrawAll(app, canvas):
    #draws shop layout
    drawBckg(app, canvas)
    #draws day information 
    drawInfo(app, canvas)
    
    if app.hasOrder and app.isThereCust:
        #kitchen button display
        if app.hasChefBooster:
            canvas.create_image(800, 395, image=ImageTk.PhotoImage(app.chefBoba.rotate(angle=10)))
        drawButton(canvas, app.shop_kitchenBtnDms, 'Kitchen')
    
    if app.isThereCust:
        #draws customer
        drawCust(app, canvas)
        
    #draws order   
    if app.hasTakenOrder and app.isThereCust:
        drawOrder(app, canvas)   

def drawBckg(app, canvas):
    #background image
    canvas.create_image(375, 200, image=ImageTk.PhotoImage(app.shopBckg))
    
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, fill='black', width=3)
    
    #blue sidebar
    canvas.create_rectangle(750, 0, app.width, app.height, fill='lightblue1', width=0)
    
    #countertop
    canvas.create_line(0, app.height*(2/3), app.width*(3/4), app.height*(2/3), fill='black', width=3)
    canvas.create_image(375, 500, image=ImageTk.PhotoImage(app.counter))
    
    #tips jar
    canvas.create_image(650, 350, image=ImageTk.PhotoImage(scaleImage(app, app.tipsJar, (100, 100))))
    
    #cash register
    canvas.create_image(100, 335, image=ImageTk.PhotoImage(scaleImage(app, app.cashRegister, (200, 200))))
    
    #help button display
    canvas.create_image(100, 510, image=ImageTk.PhotoImage(scaleImage(app, app.helpBoba, (85, 85))))
    drawButton(canvas, app.shop_helpBtnDms, 'Help')
    
def drawInfo(app, canvas):
    #day info box
    canvas.create_rectangle(550, 10, 740, 100, width=2, fill='lightblue1')
    canvas.create_text(645, 30, text=f'Day {app.dayIndex}', font = 'Courier 15 bold')
    
    #current user display
    canvas.create_text(645, 80, text=f'Current User:', font='Courier 8 bold')
    canvas.create_text(645, 90, text=f'{app.username}', font='Courier 8 bold')
    
    #day progress bar
    canvas.create_rectangle(555, 50, 735, 70, width=3, fill='gray28')
    daySlice = (180/app.dayLength)*(app.dayLength-app.currentDay.dayTime)
    canvas.create_rectangle(556, 52, 556+daySlice, 69, width=0, fill='chartreuse4')
    
    #money
    canvas.create_text(650, 275, text= f'${roundUp(app.money, 2)}', font='Courier 25 bold')
    
    if not app.hasTakenOrder:
        canvas.create_text(875, 40, text='No Current Order', font='Courier 15 bold')
        
def drawCust(app, canvas):
    canvas.create_image(200, 300, image=ImageTk.PhotoImage(scaleImage(app, app.body, (200, 200))))
    canvas.create_image(200, 300, image=ImageTk.PhotoImage(scaleImage(app, app.neutral, (200, 200))))
    curCustImg = scaleImage(app, app.currentDay.custList[app.currentDay.custIndex-1].custImg, (200, 200))
    canvas.create_image(200, 300, image=ImageTk.PhotoImage(curCustImg))
    
    #take order button display
    if not app.hasTakenOrder:
        if app.hasBrainyBooster:
            canvas.create_image(100, 400, image=ImageTk.PhotoImage(app.moneyBoba.rotate(angle=10)))
        drawButton(canvas, app.shop_takeOrderBtnDms, 'Take Order')
    
def drawOrder(app, canvas):
    #yellow ticket
    canvas.create_rectangle(775, 25, 975, 250, fill='#eecf90', width=3)
    
    #order ticket content
    canvas.create_text(875, 40, text=f"Customer #{(app.currentDay.custIndex)}", font='Courier 20 bold')
    
    #draws customer's topping choice
    if app.orderRevealTimer > 10:
        canvas.create_text(875, 70, 
        text=app.currentDay.custList[app.currentDay.custIndex-1].order[0], font='Courier 15 bold')
    
    #draws customer's amount of sugar cubes choice
    if app.orderRevealTimer > 20:
        canvas.create_text(875, 100, 
        text=app.currentDay.custList[app.currentDay.custIndex-1].order[1], font='Courier 15 bold')

    #draws customer's amount of ice cubes choice
    if app.orderRevealTimer > 30:
        canvas.create_text(875, 130, 
        text=app.currentDay.custList[app.currentDay.custIndex-1].order[2], font='Courier 15 bold')
    
    #draws customer's milk choice
    if app.orderRevealTimer > 40:
        canvas.create_text(875, 160, 
        text=app.currentDay.custList[app.currentDay.custIndex-1].order[3], font='Courier 15 bold')
    
    #draws customer's tea choice
    if app.orderRevealTimer > 50:
        canvas.create_text(875, 190, 
        text=app.currentDay.custList[app.currentDay.custIndex-1].order[4], font='Courier 15 bold')
        
###################################    
#controller
###################################
def shopScreen_mouseReleased(app, event):
    # kitchen button check
    if isValidClick(event.x, event.y, app.shop_kitchenBtnDms) and app.hasOrder and app.isThereCust:
        app.isThereCust = False
        app.totalOrders += 1
        app.mode = 'kitchenScreen'
    elif isValidClick(event.x, event.y, app.shop_takeOrderBtnDms) and app.isThereCust:
        app.hasTakenOrder = True
    # help button check
    elif isValidClick(event.x, event.y, app.shop_helpBtnDms):
        app.curHelpScene = 2
        app.cameFromGame = True
        app.mode = 'helpScreen'
        
def shopScreen_timerFired(app):
    #reveal timer increment
    if app.hasTakenOrder:
        app.orderRevealTimer += 1
        
    if app.orderRevealTimer > 60:
        app.hasOrder = True
        
    app.currentDay.canNextCust(app)
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    checkIfGameOver(app)   