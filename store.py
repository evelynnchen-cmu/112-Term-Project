from helpers import *

class Store():
    def __init__(self, app):
        self.doneBtnDms = (800, 525, 950, 575)
    
    def drawBckg(self, app, canvas):
        canvas.create_text(app.width/2, app.height/2, text="store screen")
        
        #vertical divider
        canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                    fill='black', width=3)
        
        #horizontal divider
        canvas.create_line(0, app.height/10, app.width*(3/4), app.height/10, 
                                                    fill='black', width=3)
        #day
        canvas.create_text(50, 30, text=f'Day: {app.player.currentDay}', font='Arial 25 bold')
        #money
        canvas.create_text(250, 30, text=f'Money: ${app.player.money}', font='Arial 25 bold')
        
        drawButton(canvas, self.doneBtnDms, 'Done')
    
    def drawOptions(self, app, canvas):
        #tea title
        canvas.create_text(200, 100, text='Teas', font='Arial 20')
    
    def drawInventory(self, app, canvas):
        space = 70
        
        #Inventory title
        canvas.create_text(875, 25, text='Current Inventory', font='Arial 20 bold')
        
        #tea inventory
        canvas.create_text(875, 50, text='Teas', font='Arial 18 bold')
        for item in app.inventory.teaInventory:
            canvas.create_text(875, space, text=f'{item}: {app.inventory.teaInventory[item]}', font='Arial 18')
            space += 20
            
        #toppings inventory
        space += 20
        canvas.create_text(875, space, text='Toppings', font='Arial 18 bold')
        space += 20
        for item in app.inventory.toppingsInventory:
            canvas.create_text(875, space, text=f'{item}: {app.inventory.toppingsInventory[item]}', font='Arial 18')
            space += 20
            
        #supplies inventory
        space += 20
        canvas.create_text(875, space, text='Supplies', font='Arial 18 bold')
        space += 20
        for item in app.inventory.suppliesInventory:
            canvas.create_text(875, space, text=f'{item}: {app.inventory.suppliesInventory[item]}', font='Arial 18')
            space += 20