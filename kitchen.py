from classes import *

###################################
#view
###################################
def kitchenScreen_redrawAll(app, canvas):
        
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                fill='black', width=3)
        
    drawButton(canvas, app.kitchen_storeBtnDms, 'Store')
    drawButton(canvas, app.kitchen_evalBtnDms, 'Evaluate')
    
###################################
#controller
###################################
def kitchenScreen_mouseReleased(app, event):
    # store button
    if isValidClick(event.x, event.y, app.kitchen_storeBtnDms):
        app.mode = 'storeScreen'
    # eval button
    elif isValidClick(event.x, event.y, app.kitchen_evalBtnDms):
        app.mode = 'evaluationScreen'
        
def kitchenScreen_timerFired(app):
    checkIfGameOver(app)
    checkIfDayOver(app)
    
        