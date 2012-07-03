'''from graphics import *
# create the graphics window
win = GraphWin("Digital Clock", 300, 300)
# create a text objects centered at (100, 100)
msg1 = Text( Point( 100, 100 ), "Hello, AITI Kenya!" )
msg1.draw( win )
# process events
win.mainloop()'''

from graphics import *
# DigitalClock class definition goes here
class DigitalClock:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
        self.time=None

    def timeToString(self):
        if self.hour%24<10:
            strHour='0'+str(self.hour)
        else:
            strHour=str(self.hour)
        if self.minute%60<10:
            strMin='0'+str(self.minute)
        else:
            strMin=str(self.minute)
        if self.second%60<10:
            strSec='0'+str(self.second)
        else:
            strSec=str(self.second)
            
        return strHour+':'+strMin+':'+strSec

    def drawFace(self,win):
        face=Rectangle(Point(25,50),Point(275,150))
        face.setFill('white')
        face.draw(win)
    
    def drawText(self,win):
        self.time= Text( Point( 150, 100 ), self.timeToString() )
        self.time.setFace('courier')
        self.time.setStyle('bold italic')
        self.time.setFill('blue')
        self.time.setSize(36)
        self.time.draw( win )

    def update(self):
        self.second+=1
        if self.second >0:
            remSec=self.second%60
            if remSec==0:
                self.second=0
                self.minute+=1
        if self.minute >0:
            remMin=self.minute%60
            if remMin==0:
                self.minute=0
                self.hour+=1
        if self.hour >0:
            remHour=self.hour%24
            if remHour==0:
                self.hour=0
            
        self.time.setText(self.timeToString())

    def draw(self,win):
        self.drawFace(win)
        self.drawText(win)
        self.tick(10)

    def tick(self, n):
        if n > 0:
            self.update()
            win.after(1000, self.tick,n)
        
win = GraphWin("Digital Clock", 300, 300)
clock = DigitalClock(7, 10, 55)
clock.draw(win)
win.mainloop()

