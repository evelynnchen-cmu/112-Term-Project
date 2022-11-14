from helpers import *

class Shop():
    def __init__(self, app):
        self.takeOrderBtnDms = (25, 412.5, 175, 462.5)
        self.kitchenBtnDms = (575, 525, 725, 575)
        self.storeBtnDms = (25, 525, 175, 575)
        
        self.tipsJar = app.loadImage('./assets/tips_jar.png')
        self.tipsJarSmall = scaleImage(app, self.tipsJar, (100, 100))
    
    def drawBckg(self, app, canvas):
        canvas.create_text(app.width/2, app.height/2, text="shop screen")
        
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
        
        #counter
        canvas.create_line(0, 400, 750, 400, fill='black', width=3)
        canvas.create_rectangle(0, 400, 750, 600, fill='bisque2')
        
        #cash register
        canvas.create_rectangle(25, 325, 125, 385, fill='black')
        canvas.create_rectangle(62.5, 375, 87.5, 400, fill='black')
        canvas.create_text(75, 355, text='$$$', fill='green', font='Arial 15 bold')

        #tips jar
        canvas.create_image(650, 350, 
                image=ImageTk.PhotoImage(self.tipsJarSmall))
        
        drawButton(canvas, self.takeOrderBtnDms, 'Take Order')
        drawButton(canvas, self.kitchenBtnDms, 'Kitchen')
        drawButton(canvas, self.storeBtnDms, 'Store')