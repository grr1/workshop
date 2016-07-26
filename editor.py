
# editor.py
# This class implements a Graphical Editor
#

from graphics import *
from button import Button

class Editor:

    #Constructor for the editor
    def __init__(self):
        
        #Create a window
        self.win = GraphWin('Graphic Editor', 800, 800)

        # Make the window scaled
        self.win.setCoords(0, 0, 10.0, 10.0)

        # Create the buttons
        self.buttons = []
        self.createButtons()

        #Initial color
        self.color = "red"

        #List of figures
        self.figs = []

    # Add one button. It will be placed in the first available space
    def addButton(self, label, func):
        
        # Get button number
        buttonNum = len(self.buttons)

        #Compute ccordinate of button
        x = 1.5 * (buttonNum % 2) + 0.8
        y = 9.5 - 0.6 * (buttonNum //2) 

        #Create button
        button = Button(self.win, Point(x,y), 1.4, 0.5, label)
        button.activate()

        #Add button to list
        self.buttons.append({'button':button, 'func':func} )

    # Create all buttons in the application
    def createButtons(self):
        self.addButton("Line", self.newLine)
        self.addButton("Rectangle", self.newRectangle)

        colors = ["red", "blue", "green", "yellow", "pink", "brown"]
        for c in colors:
            self.addButton(c, self.setColor)

    # Chec for mouse events
    def run(self):
        while True:
            # Wait until we click mouse in the window
            p = self.win.getMouse()

            # Check if a button was pressed
            for e in self.buttons:
                b = e['button']
                if b.clicked(p):
                    # This button was pressed. Invoke function.
                    print(b.getLabel())
                    func = e['func']
                    func(b.getLabel())
                    
    ##### Commands in the editor ####
    def newLine(self, cmd):
        print("---- New Line ----")
        
        print("Press first point")
        p1 = self.win.getMouse()

        print("Press last point")
        p2 = self.win.getMouse()

        # Create Line
        line = Line(p1, p2)
        line.setFill(self.color)
        line.setWidth(5)
        line.draw(self.win)

        # Add to list of figures
        self.figs.append(line)

    def newRectangle(self,cmd):
        print("---- New Rectangle ---")
        
        print("Press Corner 1")
        c1 = self.win.getMouse()
        print("Press Corner 2")
        c2 = self.win.getMouse()

        #Create rectangle
        rect = Rectangle(c1, c2)
        rect.setFill(self.color)
        rect.draw(self.win)

        #Add to list of figures
        self.figs.append(rect)

    def setColor(self,cmd):
        print("Set Color to", cmd)
        self.color = cmd

def main():
    editor = Editor()
    editor.run()

main()

