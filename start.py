from classes import *

###################################
#view
###################################
def startScreen_redrawAll(app, canvas):
    drawButton(canvas, app.start_startBtnDms, 'Start')

###################################    
#controller
###################################
def startScreen_mouseReleased(app, event):
    # start button
    if isValidClick(event.x, event.y, app.start_startBtnDms):
        app.mode = 'shopScreen'