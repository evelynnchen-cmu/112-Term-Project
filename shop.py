from classes import *

###################################
#view
###################################
def shopScreen_redrawAll(app, canvas):

    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill='#b2beb5', width=0)
    
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, fill='black', width=3)
    #blue sidebar#dcd3fe
    canvas.create_rectangle(750, 0, app.width, app.height, fill='lightblue1', width=0)
    
    #logo
    canvas.create_image(375, 225, image=ImageTk.PhotoImage(app.logo))
        
    #horizontal divider
    # canvas.create_line(0, app.height/10, app.width*(3/4), app.height/10, fill='black', width=3)
    
    #day progress bar
    canvas.create_rectangle(225, 10, 722, 50, width=3)
    daySlice = (485/app.dayLength)*(app.dayLength-app.currentDay.dayTime)
    canvas.create_rectangle(227, 12, 227+daySlice, 49, width=0, fill='chartreuse4')
    
    #day index
    canvas.create_text(115, 30, text=f'Day {app.dayIndex}', font='Courier 20 bold')
    
    #money
    canvas.create_text(650, 275, text= f'${app.money}', font='Courier 25 bold')
        
    #counter
    canvas.create_line(0, app.height*(2/3), app.width*(3/4), app.height*(2/3), fill='black', width=3)
    canvas.create_image(375, 500, image=ImageTk.PhotoImage(app.counter))
    
    #tips jar
    canvas.create_image(650, 350, image=ImageTk.PhotoImage(scaleImage(app, app.tipsJar, (100, 100))))
        
    drawButton(canvas, app.shop_storeBtnDms, 'Store')
    
    if app.hasOrder and app.isThereCust:
        drawButton(canvas, app.shop_kitchenBtnDms, 'Kitchen')
    if not app.hasTakenOrder:
        canvas.create_text(875, 300, text='No Current Order', font='Courier 15 bold')
    
    if app.isThereCust:
        canvas.create_image(200, 300, image=ImageTk.PhotoImage(scaleImage(app, app.body, (200, 200))))
        canvas.create_image(200, 300, image=ImageTk.PhotoImage(scaleImage(app, app.neutral, (200, 200))))
        
        curCustImg = scaleImage(app, app.currentDay.custList[app.currentDay.custIndex-1].custImg, (200, 200))
        
        canvas.create_image(200, 300, image=ImageTk.PhotoImage(curCustImg))
        drawButton(canvas, app.shop_takeOrderBtnDms, 'Take Order')
    
    #cash register
    canvas.create_rectangle(32, 300, 122, 357, fill='white', width=0)
    canvas.create_image(125, 335, image=ImageTk.PhotoImage(scaleImage(app, app.cashRegister, (200, 200))))
    canvas.create_image(75, 327, image=ImageTk.PhotoImage(scaleImage(app, app.cashRegisterScreen, (63, 63))))
    
    
    
    #trademark
    canvas.create_image(965, 555, image=ImageTk.PhotoImage(scaleImage(app, app.logo, (75, 75))))
    
    #slowly reveal order    
    if app.hasTakenOrder and app.isThereCust:
        canvas.create_text(875, 20, 
            text=f"Customer #{(app.currentDay.custIndex)}", font='Courier 20 bold')   
        
        if app.orderRevealTimer > 10:
            canvas.create_text(875, 50, 
            text=app.currentDay.custList[app.currentDay.custIndex-1].order[0], font='Courier 15 bold')
        
        if app.orderRevealTimer > 20:
            canvas.create_text(875, 80, 
            text=app.currentDay.custList[app.currentDay.custIndex-1].order[1], font='Courier 15 bold')

        if app.orderRevealTimer > 30:
            canvas.create_text(875, 110, 
            text=app.currentDay.custList[app.currentDay.custIndex-1].order[2], font='Courier 15 bold')
            
        if app.orderRevealTimer > 40:
            canvas.create_text(875, 140, 
            text=app.currentDay.custList[app.currentDay.custIndex-1].order[3], font='Courier 15 bold')
            
        if app.orderRevealTimer > 50:
            canvas.create_text(875, 170, 
            text=app.currentDay.custList[app.currentDay.custIndex-1].order[4], font='Courier 15 bold')
            
    
            
        
###################################    
#controller
###################################
def shopScreen_mouseReleased(app, event):
    # kitchen button
    if isValidClick(event.x, event.y, app.shop_kitchenBtnDms) and app.hasOrder and app.isThereCust:
        app.isThereCust = False
        app.mode = 'kitchenScreen'
    # store button
    elif isValidClick(event.x, event.y, app.shop_storeBtnDms):
        app.mode = 'storeScreen'
    elif isValidClick(event.x, event.y, app.shop_takeOrderBtnDms) and app.isThereCust:
        app.totalOrders += 1
        app.hasTakenOrder = True
        
def shopScreen_timerFired(app):
    if app.hasTakenOrder:
        app.orderRevealTimer += 1
        
    if app.orderRevealTimer > 60:
        app.hasOrder = True
        
    app.currentDay.canNextCust(app)
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    
    checkIfGameOver(app)
    
        