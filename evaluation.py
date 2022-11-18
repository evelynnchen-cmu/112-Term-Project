from classes import *

###################################
#view
###################################
def evaluationScreen_redrawAll(app, canvas):
    tipsJarLarge = scaleImage(app, app.tipsJar, (200, 200))
        
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                fill='black', width=3)
        
    #counter
    canvas.create_line(0, app.height*(5/6), app.width*(3/4), app.height*(5/6), fill='black', width=3)
    canvas.create_rectangle(0, app.height*(5/6), app.width*(3/4), app.height, fill='bisque2')
        
    #tips jar
    canvas.create_image(600, 400, 
                image=ImageTk.PhotoImage(tipsJarLarge))
        
    #drink
        
    drawButton(canvas, app.eval_doneBtnDms, 'Done')

###################################    
#controller
###################################
def evaluationScreen_mouseReleased(app, event):
    # done button
    if isValidClick(event.x, event.y, app.eval_doneBtnDms):
        app.mode = 'shopScreen'
        
def evaluationScreen_timerFired(app):
    checkIfGameOver(app)
    checkIfDayOver(app)
    
    