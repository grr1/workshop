
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
        self.win.setCoords(0, 0, 10, 10)

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
        
    #######################################################
    ##### TODO 1: Find your slot and add your button ######
    #######################################################
        
        ##### Teacher 0 Add Button
        self.addButton("Line", self.newLine)
        
        ##### Teacher 1 Add Button
        self.addButton("Rectangle", self.newRectangle)
        
        ##### Teacher 2 Add Button
        self.addButton("House", self.house)
        
        ##### Teacher 3 Add Button
        
        ##### Teacher 4 Add Button
        
        ##### Teacher 5 Add Button
        self.addButton("Happy Face", self.newHappyFace)
        
        ##### Teacher 6 Add Button
        
        ##### Teacher 7 Add Button
        
        ##### Teacher 8 Add Button
        
        ##### Teacher 9 Add Button
        self.addButton("COYS", self.newTottenham)
        
        ##### Teacher 10 Add Button
        self.addButton("Sad Face", self.SadFace)
        ##### Teacher 11 Add Button
        
        self.addButton("Happy Face", self.newPeteFace)
        ##### Teacher 12 Add Button
        
        ##### Teacher 13 Add Button
        self.addButton("Oval", self.newOval)
        ##### Teacher 14 Add Button
        
        ##### Teacher 15 Add Button
        
        ##### Teacher 16 Add Button
        
        ##### Teacher 17 Add Button
        
        ##### Teacher 18 Add Button
        
        ##### Teacher 19 Add Button
        
        ##### Teacher 20 Add Button

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

    ####################################################################
    ##### TODO 2: Find your slot and add your new Figure function ######
    ####################################################################

    ##### Entry for teacher 0 - New Figure    
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

    ##### Entry for teacher 1 - New Figure  

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

    ##### Entry for teacher 2 - New Figure  
    def house(self,cmd):
        print("Press Center")
        c1 = self.win.getMouse()

        #Create wall
        wall = Rectangle(Point(c1.x-1,c1.y-1),Point(c1.x+1,c1.y+.5))
        wall.setFill("black")
        wall.draw(self.win)

        #Create door
        door = Rectangle(Point(c1.x-.4,c1.y),Point(c1.x,c1.y-1))
        door.setFill("red")
        door.draw(self.win)
        
        #Create circle window
        cir = Circle(Point(c1.x+.6,c1.y-.3), .2)
        cir.setFill("blue")
        cir.draw(self.win)

        #Create chimney
        chimney = Rectangle(Point(c1.x-.8,c1.y+.5),Point(c1.x-.6,c1.y+.8))
        chimney.setFill("black")
        chimney.draw(self.win)

    ##### Entry for teacher 3 - New Figure  

    ##### Entry for teacher 4 - New Figure  

    ##### Entry for teacher 5 - New Figure
    def newHappyFace(self,cmd):
        print("New Happy Face...");
        print("Press Center")
        c1 = self.win.getMouse()

        #Draw Face
        circle = Circle(c1, 1)
        circle.setFill("yellow")
        circle.draw(self.win)

        #Draw smile
        mouth = Circle(Point(c1.x,c1.y-.3), .6);
        mouth.setFill("black")
        mouth.draw(self.win)
        mouth2 = Circle(Point(c1.x,c1.y), .6);
        mouth2.setFill("yellow")
        mouth2.setOutline("yellow");
        mouth2.draw(self.win)

        #draw eyes
        eye1 = Circle(Point(c1.x-.3,c1.y+.3), .2);
        eye1.setFill("black")
        eye1.draw(self.win)
        eye2 = Circle(Point(c1.x+.3,c1.y+.3), .2);
        eye2.setFill("black")
        eye2.draw(self.win)

    def SadFace(self,cmd):
        print("Sad Face...");
        print("Press Center")
        c1 = self.win.getMouse()

        #Draw Face
        circle = Circle(c1, 1)
        circle.setFill("blue")
        circle.draw(self.win)

        #Draw smile
        mouth = Circle(Point(c1.x,c1.y-.3), .6);
        mouth.setFill("black")
        mouth.draw(self.win)
        mouth2 = Circle(Point(c1.x,c1.y), .6);
        mouth2.setFill("blue")
        mouth2.setOutline("blue");
        mouth2.draw(self.win)

        #draw eyes
        eye1 = Circle(Point(c1.x-.3,c1.y+.3), .2);
        eye1.setFill("black")
        eye1.draw(self.win)
        eye2 = Circle(Point(c1.x+.3,c1.y+.3), .2);
        eye2.setFill("black")
        eye2.draw(self.win)

 
    ##### Entry for teacher 6 - New Figure  

    ##### Entry for teacher 7 - New Figure  

    ##### Entry for teacher 8 - New Figure  

    ##### Entry for teacher 9 - New Figure
    def newTottenham(self,cmd):
        print("---- COYS = Come On Ye Spurs !!! ---")
        
        print("Press where you want the Spurs logo to display")
        c1 = self.win.getMouse()

           
        print("Press where you want Harry Kane to display")
        c2 = self.win.getMouse()
        

        # Create images
        logo = Image(c1, "spurs.gif")
        harry = Image(c2, "hk.gif")     
        # Set the images
        logo.draw(self.win)
        harry.draw(self.win)

    ##### Entry for teacher 10 - New Figure  

    ##### Entry for teacher 11 - New Figure  
    def newPeteFace(self,cmd):
        print("New Happy Face...");
        print("Press Center")
        c1 = self.win.getMouse()

        #Draw Face
        circle = Circle(c1, 1)
        circle.setFill("red")
        circle.draw(self.win)

        #Draw smile
        mouth = Circle(Point(c1.x,c1.y-.3), .6);
        mouth.setFill("white")
        mouth.draw(self.win)
        mouth2 = Circle(Point(c1.x,c1.y), .6);
        mouth2.setFill("red")
        mouth2.setOutline("red");
        mouth2.draw(self.win)

        #draw eyes
        eye1 = Oval(Point(c1.x-.3,c1.y+.2), Point(c1.x-.3,c1.y+.2));
        eye1.setFill("white")
        eye1.draw(self.win)
        eye2 = Oval(Point(c1.x+.3,c1.y+.2), Point(c1.x+.3,c1.y+.2));
        eye2.setFill("white")
        eye2.draw(self.win)

    ##### Entry for teacher 12 - New Figure  

    ##### Entry for teacher 13 - New Figure  
    def newOval(self,cmd):
        print("---- New Oval ---")
            
        print("Press Corner 1")
        c1 = self.win.getMouse()
        print("Press Corner 2")
        c2 = self.win.getMouse()

        #Create oval
        ov = Oval(c1, c2)
        ov.setFill(self.color)
        ov.draw(self.win)
       
    ##### Entry for teacher 14 - New Figure  

    ##### Entry for teacher 15 - New Figure  

    ##### Entry for teacher 16 - New Figure  

    ##### Entry for teacher 17 - New Figure  

    ##### Entry for teacher 18 - New Figure  

    ##### Entry for teacher 19 - New Figure  
        
    ##### Entry for teacher 20 - New Figure  

    def setColor(self,cmd):
        print("Set Color to", cmd)
        self.color = cmd

def main():
    editor = Editor()
    editor.run()

main()

