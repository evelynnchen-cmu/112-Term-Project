from classes import *

###################################
#view
###################################
def dayOverScreen_redrawAll(app, canvas):

    drawBckg(app, canvas)
    drawDayResults(app, canvas)
    
    if app.dayOverRevealTimer > 70:
        #next day button display
        drawButton(canvas, app.dayOver_nextDayBtnDms, 'Next Day')

def drawBckg(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    canvas.create_image(150, 350, image=ImageTk.PhotoImage(app.boba))
    canvas.create_image(850, 350, image=ImageTk.PhotoImage(app.boba))

def drawDayResults(app, canvas):
    
    if app.dayOverRevealTimer > 10:
        canvas.create_rectangle(300, 100, 700, 500, fill='#eecf90', width=3)
    
    if app.dayOverRevealTimer > 20:
        canvas.create_text(500, 130, text=f"Day {app.dayIndex} Results", font='Courier 25 bold underline')
    
    if app.dayOverRevealTimer > 30:
        canvas.create_text(500, 170, text="Number of Customers Served:", font='Courier 18 bold') 
        
    if app.dayOverRevealTimer > 40:
        canvas.create_text(500, 220, text=f"{app.currentDay.custIndex-1}/{app.currentDay.numOfCusts}", 
                        font='Courier 25 bold')
    
    if app.dayOverRevealTimer > 50:
        canvas.create_text(500, 270, text=f'Average Score:', font='Courier 18 bold')
        
    if app.dayOverRevealTimer > 60:
        canvas.create_text(500, 320, text=f'{app.avgScore*100}%', font='Courier 25 bold')

###################################    
#controller
###################################
def dayOverScreen_mouseReleased(app, event):
    # next day button check
    if isValidClick(event.x, event.y, app.dayOver_nextDayBtnDms) and app.dayOverRevealTimer > 70:
        startNewDay(app)
        app.mode = 'shopScreen'
        
def dayOverScreen_timerFired(app):
    app.dayOverRevealTimer += 1       