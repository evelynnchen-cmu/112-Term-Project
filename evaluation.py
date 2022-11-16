from helpers import *

###################################
#view
###################################
def evaluationScreen_redrawAll(app, canvas):
    tipsJarLarge = scaleImage(app, app.tipsJar, (200, 200))
        
    #vertical divider
    canvas.create_line(app.width*(3/4), 0, app.width*(3/4), app.height, 
                                                fill='black', width=3)
        
    #counter
    canvas.create_line(0, 500, 750, 500, fill='black', width=3)
    canvas.create_rectangle(0, 500, 750, 600, fill='bisque2')
        
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