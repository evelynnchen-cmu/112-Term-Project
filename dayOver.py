from classes import *

###################################
#view
###################################
def dayOverScreen_redrawAll(app, canvas):
    drawButton(canvas, app.dayOver_nextDayBtnDms, 'Next Day')

###################################    
#controller
###################################
def dayOverScreen_mouseReleased(app, event):
    # next day button
    if isValidClick(event.x, event.y, app.dayOver_nextDayBtnDms):
        startNewDay(app)
        app.mode = 'shopScreen'
        
        