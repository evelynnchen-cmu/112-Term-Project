from classes import *

###################################
#view
###################################
def helpScreen_redrawAll(app, canvas):
    #background color
    canvas.create_rectangle(0, 0, app.width, app.height, fill= '#b0906f', width=0)
    #changes the current help scene screen
    if app.curHelpScene == 1:
        drawGameHelp(app, canvas)
    elif app.curHelpScene == 2:
        drawShopHelp(app, canvas)
    elif app.curHelpScene == 3:
        drawKitchenHelp(app, canvas)
    elif app.curHelpScene == 4:
        drawEvalHelp(app, canvas)
    elif app.curHelpScene == 5:
        drawStoreHelp(app, canvas)
    
    #if the user came from the game, they should only see their current screen's help screen
    if not app.cameFromGame:    
        if app.curHelpScene == 5:
            drawButton(canvas, app.help_doneBtnDms, 'Done')
        else:
            drawButton(canvas, app.help_nextBtnDms, 'Next')
            
        if app.curHelpScene != 1:
            drawButton(canvas, app.help_backBtnDms, 'Back')
    else:
        drawButton(canvas, app.help_doneBtnDms, 'Go to Game')
    
def drawGameHelp(app, canvas):
    canvas.create_text(500, 100, text="Welcome to Evelynn's Bobaria!", font='Courier 35 bold')
    canvas.create_image(700, 300, image=ImageTk.PhotoImage(app.happyBoba))
    canvas.create_text(450, 300, text=
        """
        Your journey to becoming a master bobarista begins today.\n\n
        As a bobarista at Evelynn's Bobaria, you must do the following:\n
        1. Take the customer's order.\n
        2. Make the drink as accurate as possible.\n
        3. Present the drink to the customer for evaluation.\n\n
        Click 'Next' to visit the shop and see how the masters do it!
        """, font='Courier 15 bold')
    
def drawShopHelp(app, canvas):
    canvas.create_text(500, 25, text='Shop Screen', font='Courier 25 bold')
    canvas.create_image(275, 290, image=ImageTk.PhotoImage(app.moneyBoba.rotate(angle=5)))
    canvas.create_text(250, 175, text="""
        Sit behind the counter and wait\n
        until a customer appears. When they\n
        do, click on 'Take Order' to take\n
        their order.
        """, font='Courier 13 bold')
    canvas.create_image(700, 175, image=ImageTk.PhotoImage(scaleImage(app, app.isCustScene, (400, 225))))
    canvas.create_rectangle(511, 62, 891, 289, width=2)
    
    canvas.create_text(225, 400, text="""
        Once you have their order,\n
        click on 'Kitchen' to go make it.
        """, font='Courier 13 bold')
    canvas.create_image(700, 425, image=ImageTk.PhotoImage(scaleImage(app, app.gotOrderScene, (400, 225))))
    canvas.create_rectangle(511, 312, 891, 538, width=2)
    
def drawKitchenHelp(app, canvas):
    canvas.create_text(500, 25, text='Kitchen Screen', font='Courier 25 bold')
    canvas.create_image(445, 280, image=ImageTk.PhotoImage(app.chefBoba))
    canvas.create_text(250, 175, text="""
        Click and drag each ingredient over to\n
        the cup to add it to the drink.\n
        Be accurate with how much you add.\n
        Customers are more lenient at first,\n
        but won't be for very long...
        """, font='Courier 13 bold')
    canvas.create_image(700, 175, image=ImageTk.PhotoImage(scaleImage(app, app.addIngScene, (400, 225))))
    canvas.create_rectangle(511, 62, 891, 289, width=2)
    
    canvas.create_text(225, 400, text="""
        Once you add all the ingredients,\n
        click 'Mix' to mix the drink.\n
        Then click 'Evaluate' to present\n
        the ready-drink to the customer.
        """, font='Courier 13 bold')
    canvas.create_image(700, 425, image=ImageTk.PhotoImage(scaleImage(app, app.mixedDrinkScene, (400, 225))))
    canvas.create_rectangle(511, 312, 891, 538, width=2)
    
def drawEvalHelp(app, canvas):
    canvas.create_text(500, 25, text='Evaluation Screen', font='Courier 25 bold')
    canvas.create_image(440, 250, image=ImageTk.PhotoImage(app.searchingBoba.rotate(angle=-5)))
    canvas.create_text(250, 175, text="""
        Let the customer evaluate the drink\n
        and calculate its score and their tip.\n
        Remember, customers are impatient. The\n
        quicker you are, the more tips you\n 
        receive!
        """, font='Courier 13 bold')
    canvas.create_image(700, 175, image=ImageTk.PhotoImage(scaleImage(app, app.custCritiqueScene, (400, 225))))
    canvas.create_rectangle(511, 62, 891, 289, width=2)
    
    canvas.create_text(240, 400, text="""
        You'll be able to see the results on\n
        the right-hand side. Click 'Done' to\n
        return to the shop counter.
        """, font='Courier 13 bold')
    canvas.create_image(700, 425, image=ImageTk.PhotoImage(scaleImage(app, app.custEvalScene, (400, 225))))
    canvas.create_rectangle(511, 312, 891, 538, width=2)

def drawStoreHelp(app, canvas):
    canvas.create_text(500, 25, text='Boba Baby Booster Store', font='Courier 25 bold')
    canvas.create_image(385, 410, image=ImageTk.PhotoImage(app.heartBoba.rotate(angle=-5)))
    canvas.create_text(225, 300, text="""
        At the end of every day, you'll be\n
        able to browse the Boba Baby Booster\n
        Store! Here you can purchase Boba Babies\n
        that give you certain boosts and make your\n 
        job a tad easier. They'll also keep you\n
        company throughout the day.
        """, font='Courier 13 bold')
    
    canvas.create_image(700, 300, image=ImageTk.PhotoImage(scaleImage(app, app.selectedStoreScene, (400, 225))))
    canvas.create_rectangle(500, 185, 900, 413, width=2)
###################################
#controller
###################################
        
def helpScreen_mouseReleased(app, event):
    # next button check
    if isValidClick(event.x, event.y, app.help_nextBtnDms) and app.curHelpScene < 5 and not app.cameFromGame:
        app.curHelpScene += 1
    # back button check
    if isValidClick(event.x, event.y, app.help_backBtnDms) and app.curHelpScene > 1 and not app.cameFromGame:
        app.curHelpScene -= 1
    #done button
    if isValidClick(event.x, event.y, app.help_doneBtnDms) and (app.curHelpScene == 5 or app.cameFromGame):
        if not app.cameFromGame:
            app.mode = 'startScreen'
        else:
            if app.curHelpScene == 2:
                app.mode = 'shopScreen'
            elif app.curHelpScene == 3:
                app.mode = 'kitchenScreen'
            elif app.curHelpScene == 4:
                app.mode = 'evaluationScreen'
            elif app.curHelpScene == 5:
                app.mode = 'storeScreen'