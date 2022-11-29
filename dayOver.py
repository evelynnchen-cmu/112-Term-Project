from classes import *

###################################
#view
###################################
def dayOverScreen_redrawAll(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    
    #day's stats
    canvas.create_text(500, 50, text=f"Day {app.dayIndex}'s Statistics", font='Courier 30 bold underline')
    canvas.create_text(500, 100, 
        text=f"Number of Customers Served: {app.currentDay.custIndex-1}/{app.currentDay.numOfCusts}", 
                        font='Courier 20')
    canvas.create_text(500, 150, text=f'Average Score: {app.avgScore*100}%', font='Courier 20')
    
    canvas.create_image(250, 350, image=ImageTk.PhotoImage(app.boba))
    canvas.create_image(750, 350, image=ImageTk.PhotoImage(app.boba))
    
    #next day button display
    drawButton(canvas, app.dayOver_nextDayBtnDms, 'Next Day')

###################################    
#controller
###################################
def dayOverScreen_mouseReleased(app, event):
    # next day button check
    if isValidClick(event.x, event.y, app.dayOver_nextDayBtnDms):
        startNewDay(app)
        app.mode = 'shopScreen'
        
        