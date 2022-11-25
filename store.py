from classes import *

###################################
#view
###################################
def storeScreen_redrawAll(app, canvas):
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                fill='black', width=3)
    
    #horizontal divider
    canvas.create_line(0, app.height/10, app.width*(3/4), app.height/10, 
                                                fill='black', width=3)
    #day progress bar
    canvas.create_rectangle(15, 10, 502, 50, width=3)
    daySlice = (485/app.dayLength)*(app.dayLength-app.currentDay.dayTime)
    canvas.create_rectangle(17, 12, 17+daySlice, 49, width=0, fill='chartreuse4')
    canvas.create_text(257.5, 30, text=f'Day {app.dayIndex}', font='Courier 15 bold')
   
    #money
    canvas.create_text(650, 30, text=f'${app.money}', font='Courier 25 bold')
    
    drawButton(canvas, app.eval_doneBtnDms, 'Done')
    
    #!items
    #toppings
    drawButton(canvas, (25, 75, 150, 175), 'Tapioca')
    tapioca = scaleImage(app, app.tapioca, (150, 150))
    canvas.create_image(75, 125, image=ImageTk.PhotoImage(tapioca))
    drawButton(canvas, (25, 200, 150, 300), 'Aloe Jelly')
    drawButton(canvas, (25, 325, 150, 425), 'Red Bean')
    drawButton(canvas, (25, 450, 150, 550), 'Pudding')
    
    #tea
    drawButton(canvas,(200, 75, 325, 175), 'Green Tea')
    drawButton(canvas,(200, 200, 325, 300), 'Black Tea')
    drawButton(canvas,(200, 325, 325, 425), 'Oolong Tea')
    
    #supplies
    drawButton(canvas,(375, 75, 500, 175), 'Cups')
    drawButton(canvas,(375, 200, 500, 300), 'Straws')
    drawButton(canvas,(375, 325, 500, 425), 'Seals')
    
    #!inventory
    space = 70
    #Inventory title
    canvas.create_text(875, 25, text='Current Inventory', font='Courier 20 bold')
    
    #tea 
    canvas.create_text(875, 50, text='Teas', font='Courier 18 bold')
    for item in app.teaInventory:
        canvas.create_text(875, space, text=f'{item}: {app.teaInventory[item]}', font='Courier 18')
        space += 20
         
    #toppings
    space += 20
    canvas.create_text(875, space, text='Toppings', font='Courier 18 bold')
    space += 20
    for item in app.toppingsInventory:
        canvas.create_text(875, space, text=f'{item}: {app.toppingsInventory[item]}', font='Courier 18')
        space += 20
        
    #supplies
    space += 20
    canvas.create_text(875, space, text='Supplies', font='Courier 18 bold')
    space += 20
    for item in app.suppliesInventory:
        canvas.create_text(875, space, text=f'{item}: {app.suppliesInventory[item]}', font='Courier 18')
        space += 20
        
###################################
#controller
###################################
        
def storeScreen_mouseReleased(app, event):
    #done button
    if isValidClick(event.x, event.y, app.store_doneBtnDms):
        app.mode = 'shopScreen'
    
    #tapioca button
    if isValidClick(event.x, event.y, (25, 75, 150, 175)):
        app.toppingsInventory["tapioca"] += 20
        app.money -= 20
    
    #aloe jelly button
    if isValidClick(event.x, event.y, (25, 200, 150, 300)):
        app.toppingsInventory["aloe_jelly"] += 20
        app.money -= 20
    
    #red bean button       
    if isValidClick(event.x, event.y, (25, 325, 150, 425)):
        app.toppingsInventory["red_bean"] += 20
        app.money -= 20
    
    #pudding button
    if isValidClick(event.x, event.y, (25, 450, 150, 550)):
        app.toppingsInventory["pudding"] += 20
        app.money -= 20
    
    #green tea button
    if isValidClick(event.x, event.y, (200, 75, 325, 175)):
        app.teaInventory["green_tea"] += 20
        app.money -= 20
    
    #black tea button
    if isValidClick(event.x, event.y, (200, 200, 325, 300)):
        app.teaInventory["black_tea"] += 20
        app.money -= 20
    
    #oolong tea button
    if isValidClick(event.x, event.y, (200, 325, 325, 425)):
        app.teaInventory["oolong_tea"] += 20
        app.money -= 20
    
    #cups button
    if isValidClick(event.x, event.y, (375, 75, 500, 175)):
        app.suppliesInventory["cups"] += 20
        app.money -= 20
    
    #straws button
    if isValidClick(event.x, event.y, (375, 200, 500, 300)):
        app.suppliesInventory["straws"] += 20
        app.money -= 20
    
    if isValidClick(event.x, event.y, (375, 325, 500, 425)):
        app.suppliesInventory["seals"] += 20
        app.money -= 20
        
def storeScreen_timerFired(app):
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    checkIfGameOver(app)
    
    
    
        