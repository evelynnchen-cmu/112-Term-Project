from cmu_112_graphics import *

def drawButton(canvas, dimensionTuple, buttonName):
    x0, y0, x1, y1 = dimensionTuple
    buttonWidth = abs(x0-x1)
    buttonHeight = abs(y0-y1)
    canvas.create_rectangle(x0, y0, x1, y1, fill = 'lightblue1', width = 3)
    canvas.create_text(x0 + (buttonWidth/2), y0 + (buttonHeight/2), text = buttonName, 
                            font = 'Arial 15 bold', fill = 'black')

def isValidClick(x, y, dimensionTuple):
    x0, y0, x1, y1 = dimensionTuple
    if (x0 < x < x1) and (y0 < y < y1):
        return True
    return False

# copied from TA Mini-Lecture: Advanced Tkinter Mini Lecture
def scaleImage(app, image, box):
    
    originalWidth, originalHeight = image.size
    originalRatio = originalWidth/originalHeight
    width, height = box
    goalRatio = width/height
    
    if originalRatio > goalRatio:
        scale = width/originalWidth
    else:
        scale = height/originalHeight
    
    return app.scaleImage(image, scale)