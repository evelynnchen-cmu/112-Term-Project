from helpers import *

class Kitchen():
    def __init__(self, app):

        self.storeBtnDms = (25, 525, 175, 575)
        self.evalBtnDms = (800, 525, 950, 575)
    
    def drawBckg(self, app, canvas):
        canvas.create_text(app.width/2, app.height/2, text="kitchen screen")
        
        #vertical divider
        canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                    fill='black', width=3)
        
        drawButton(canvas, self.storeBtnDms, 'Store')
        drawButton(canvas, self.evalBtnDms, 'Evaluate')