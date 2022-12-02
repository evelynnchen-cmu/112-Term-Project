from classes import *

###################################
#view
###################################
def startScreen_redrawAll(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    
    #title
    canvas.create_text(app.width//2, app.height//3, text="Evelynn's Bobaria", font='Courier 50 bold')
    
    #bobas
    canvas.create_image(250, 350, image=ImageTk.PhotoImage(app.boba))
    canvas.create_image(750, 350, image=ImageTk.PhotoImage(app.boba))
    
    if app.visitedHelp:
        #start button display
        drawButton(canvas, app.start_startBtnDms, 'Start')
    
    #how to play button display
    drawButton(canvas, app.start_howToPlayBtnDms, 'How To Play')
    
    #exit button display
    drawButton(canvas, app.start_exitBtnDms, 'Exit')

###################################    
#controller
###################################
def startScreen_mouseReleased(app, event):
    # start button check
    if isValidClick(event.x, event.y, app.start_startBtnDms) and app.visitedHelp:
        app.mode = 'shopScreen'
    elif isValidClick(event.x, event.y, app.start_howToPlayBtnDms):
        app.visitedHelp = True
        app.curHelpScene = 1
        app.mode = 'helpScreen'
    # exit button check
    elif isValidClick(event.x, event.y, app.start_exitBtnDms):
        #?copied from cmu_112_graphics.py
        os._exit(0)