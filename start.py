from classes import *

###################################
#view
###################################
def startScreen_redrawAll(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    canvas.create_text(app.width//2, app.height//3, text="Evelynn's Bobaria", font='Courier 50 bold')
    canvas.create_image(250, 350, image=ImageTk.PhotoImage(app.boba))
    canvas.create_image(750, 350, image=ImageTk.PhotoImage(app.boba))
    drawButton(canvas, app.start_startBtnDms, 'Start')

###################################    
#controller
###################################
def startScreen_mouseReleased(app, event):
    # start button
    if isValidClick(event.x, event.y, app.start_startBtnDms):
        app.mode = 'shopScreen'