from classes import *

###################################
#view
###################################
def shopScreen_redrawAll(app, canvas):
    
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, fill='black', width=3)
        
    #horizontal divider
    canvas.create_line(0, app.height/10, app.width*(3/4), app.height/10, fill='black', width=3)
    
    #day progress bar
    canvas.create_rectangle(15, 10, 502, 50, width=3)
    daySlice = (485/app.dayLength)*(app.dayLength-app.currentDay.dayTime)
    canvas.create_rectangle(17, 12, 17+daySlice, 49, width=0, fill='chartreuse4')
    canvas.create_text(257.5, 30, text=f'Day {app.dayIndex}', font='Arial 15 bold')
    
    #money
    canvas.create_text(650, 30, text= f'${app.money}', font='Arial 25 bold')
        
    #counter
    canvas.create_line(0, app.height*(5/6), app.width*(3/4), app.height*(5/6), fill='black', width=3)
    canvas.create_rectangle(0, app.height*(2/3), app.width*(3/4), app.height, fill='bisque2')
        
    #cash register
    canvas.create_rectangle(25, 325, 125, 385, fill='black')
    canvas.create_rectangle(62.5, 375, 87.5, 400, fill='black')
    canvas.create_text(75, 355, text='$$$', fill='green', font='Arial 15 bold')

    #tips jar
    tipsJarSmall = scaleImage(app, app.tipsJar, (100, 100))
    canvas.create_image(650, 350, image=ImageTk.PhotoImage(tipsJarSmall))
        
    drawButton(canvas, app.shop_storeBtnDms, 'Store')
    
    if app.hasOrder and app.isThereCust:
        drawButton(canvas, app.shop_kitchenBtnDms, 'Kitchen')

    if app.isThereCust:
        curCustImg = scaleImage(app, app.currentDay.custList[app.currentDay.custIndex].custImg, (200, 200))
        # curCustImg = app.currentDay.custList[app.currentDay.custIndex].custImg
        canvas.create_image(200, 325, image=ImageTk.PhotoImage(curCustImg))
        drawButton(canvas, app.shop_takeOrderBtnDms, 'Take Order')
    
    #slowly reveal order    
    if app.hasTakenOrder and app.isThereCust:
        canvas.create_text(875, 20, 
            text=f"Customer #{(app.currentDay.custIndex)+1}", font='Arial 20 bold')   
        
        if app.orderRevealTimer > 10:
            canvas.create_text(875, 50, 
            text=app.currentDay.custList[app.currentDay.custIndex].order[0], font='Arial 15 bold')
        
        if app.orderRevealTimer > 20:
            canvas.create_text(875, 80, 
            text=app.currentDay.custList[app.currentDay.custIndex].order[1], font='Arial 15 bold')

        if app.orderRevealTimer > 30:
            canvas.create_text(875, 110, 
            text=app.currentDay.custList[app.currentDay.custIndex].order[2], font='Arial 15 bold')
            
        if app.orderRevealTimer > 40:
            canvas.create_text(875, 140, 
            text=app.currentDay.custList[app.currentDay.custIndex].order[3], font='Arial 15 bold')
            
        if app.orderRevealTimer > 50:
            canvas.create_text(875, 170, 
            text=app.currentDay.custList[app.currentDay.custIndex].order[4], font='Arial 15 bold')
            
        
###################################    
#controller
###################################
def shopScreen_mouseReleased(app, event):
    # kitchen button
    if isValidClick(event.x, event.y, app.shop_kitchenBtnDms) and app.hasOrder and app.isThereCust:
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
        
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    app.currentDay.canNextCust(app)
    checkIfGameOver(app)
    
        