from classes import *

#?referenced https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#ioMethods
#?for getting user input
###################################
#view
###################################
def nameScreen_redrawAll(app, canvas):
    #background
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    canvas.create_image(150, 350, image=ImageTk.PhotoImage(app.boba))
    canvas.create_image(850, 350, image=ImageTk.PhotoImage(app.boba))
    
    #title
    canvas.create_text(500, 175, text="Evelynn's Bobaria", font='Courier 50 bold')
    
    #ask for name
    canvas.create_text(500, 250, text='Please type in your name to\nsave or retrieve your progress', font='Courier 15 bold')
    
    #username display
    canvas.create_rectangle(250, 300, 750, 350, width=3, fill='#eecf90')
    canvas.create_text(500, 325, text=app.username, font='Courier 20 bold')
    
def nameScreen_keyPressed(app, event):
    if event.key == 'Enter':
        # checkForProgress(app)
        app.mode = 'gameOverScreen'
    elif event.key == 'Space':
        app.username += ' '
    else:
        app.username += event.key
    

###################################    
#controller
###################################
def nameScreen_mouseReleased(app, event):
    pass