from helpers import *

#view
def storeScreen_redrawAll(app, canvas):
    #bckg
    canvas.create_text(app.width/2, app.height/2, text="store screen")
        
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                fill='black', width=3)
    
    #horizontal divider
    canvas.create_line(0, app.height/10, app.width*(3/4), app.height/10, 
                                                fill='black', width=3)
    #day
    canvas.create_text(50, 30, text=f'Day: {app.currentDay}', font='Arial 25 bold')
    #money
    canvas.create_text(250, 30, text=f'Money: ${app.money}', font='Arial 25 bold')
    
    drawButton(canvas, app.eval_doneBtnDms, 'Done')
    
    #inventory
    space = 70
    #Inventory title
    canvas.create_text(875, 25, text='Current Inventory', font='Arial 20 bold')
    
    #tea inventory
    canvas.create_text(875, 50, text='Teas', font='Arial 18 bold')
    for item in app.teaInventory:
        canvas.create_text(875, space, text=f'{item}: {app.teaInventory[item]}', font='Arial 18')
        space += 20
         
    #toppings inventory
    space += 20
    canvas.create_text(875, space, text='Toppings', font='Arial 18 bold')
    space += 20
    for item in app.toppingsInventory:
        canvas.create_text(875, space, text=f'{item}: {app.toppingsInventory[item]}', font='Arial 18')
        space += 20
        
    #supplies inventory
    space += 20
    canvas.create_text(875, space, text='Supplies', font='Arial 18 bold')
    space += 20
    for item in app.suppliesInventory:
        canvas.create_text(875, space, text=f'{item}: {app.suppliesInventory[item]}', font='Arial 18')
        space += 20
        

#controller
def storeScreen_keyPressed(app, event):
    #for testing
    if event.key == 'b':
        app.money -= 2
        app.teaInventory['black_tea'] += 1
        
def storeScreen_mouseReleased(app, event):
    # done button
    if isValidClick(event.x, event.y, app.store_doneBtnDms):
        app.mode = 'shopScreen'
        