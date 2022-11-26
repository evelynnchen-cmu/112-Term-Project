from classes import *

###################################
#view
###################################
def dayOverScreen_redrawAll(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    
    canvas.create_text(500, 50, text=f"Day {app.dayIndex}'s Statistics", font='Courier 30 bold underline')
    canvas.create_text(500, 100, 
        text=f"Number of Customers Served: {app.currentDay.custIndex-1}/{app.currentDay.numOfCusts}", 
                        font='Courier 20')
    canvas.create_text(500, 150, text=f'Average Score: {app.avgScore}', font='Courier 20')
    
    drawButton(canvas, app.dayOver_nextDayBtnDms, 'Next Day')
    
    #trademark
    canvas.create_image(965, 555, image=ImageTk.PhotoImage(scaleImage(app, app.logo, (75, 75))))

###################################    
#controller
###################################
def dayOverScreen_mouseReleased(app, event):
    # next day button
    if isValidClick(event.x, event.y, app.dayOver_nextDayBtnDms):
        startNewDay(app)
        app.mode = 'shopScreen'
        
        