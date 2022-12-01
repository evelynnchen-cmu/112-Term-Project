from classes import *

###################################
#view
###################################
def helpScreen_redrawAll(app, canvas):
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
    
    drawButton(canvas, app.help_doneBtnDms, 'Done')
        
###################################
#controller
###################################
        
def helpScreen_mouseReleased(app, event):
    #done button
    if isValidClick(event.x, event.y, app.help_doneBtnDms):
        app.mode = 'shopScreen'
        
def helpScreen_timerFired(app):
    app.currentDay.checkIfAddCust(app)
    app.currentDay.incCustWaitTime()
    app.currentDay.checkIfDayOver(app)
    checkIfGameOver(app)