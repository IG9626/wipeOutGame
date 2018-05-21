class Blocks(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.hover = False

    def display(self):
        stroke(0)
       
        rectMode(CENTER)
        if self.hover:
            fill(self.c +100)
        else:
            fill(self.c)
        rect(self.xpos, self.ypos, 20, 20);
        myBlocks1 = Blocks(color(255, 0, 0), 0, 100)
        myBlocks2 = Blocks(color(0, 255, 255), 0, 10)
    
    def setup():
        size(200,200)
    
    def draw(): 
        background(255)
        myCar1.drive()
        myCar1.display()
        
    def click(self):
        hover=mouseX>self.xpos and mouseX<self.xpos+20 and mouseY>self.ypos and mouseY<self.ypos+20