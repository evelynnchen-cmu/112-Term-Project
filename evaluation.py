from helpers import *

class Evaluation():
    def __init__(self, app):
        self.doneBtnDms = (800, 525, 950, 575)
        self.tipsJar = app.loadImage('./assets/tips_jar.png')
        self.tipsJarLarge = scaleImage(app, self.tipsJar, (200, 200))
    
    def drawBckg(self, app, canvas):
        canvas.create_text(app.width/2, app.height/2, text="evaluation screen")
        
        #vertical divider
        canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                    fill='black', width=3)
        
        #counter
        canvas.create_line(0, 500, 750, 500, fill='black', width=3)
        canvas.create_rectangle(0, 500, 750, 600, fill='bisque2')
        
        #tips jar
        canvas.create_image(600, 400, 
                image=ImageTk.PhotoImage(self.tipsJarLarge))
        
        #drink
        
        drawButton(canvas, self.doneBtnDms, 'Done')