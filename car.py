'''from graphics import *
win = GraphWin("Rectangle", 300, 300)
rect = Rectangle( Point( 10,10), Point(100, 100 ) )
rect.setFill( "blue" )
rect.setOutline('red')
rect.setWidth(2)
rect.draw( win )
win.mainloop()'''
from graphics import *
class Wheel(object):
    def __init__(self, center, wheel_radius, tire_radius):
        self.tire_circle = Circle(center, tire_radius)
        self.wheel_circle = Circle(center, wheel_radius)
    def draw(self, win):
        self.wheel_circle.draw(win)
        self.tire_circle.draw(win)
        
    def move(self, dx, dy):
        self.tire_circle.move(dx, dy)
        self.wheel_circle.move(dx, dy)
    def set_color(self, wheel_color, tire_color):
        self.tire_circle.setFill(tire_color)
        self.wheel_circle.setFill(wheel_color)
    def undraw(self):
        self.tire_circle .undraw()
        self.wheel_circle .undraw()
    def get_size(self):
        return self.tire_circle.getRadius()
    def get_center(self):
        return self.tire_circle.getCenter()
    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(100, self.animate, win, dx, dy, n-1)



win = GraphWin('Car', 700, 300)
# create a car object
class Car(object):
    def __init__(self, wheel1_center, wheel1_radius, wheel2_center, wheel2_radius,rect_height):
        self.first_wheel = Wheel(wheel1_center,wheel1_radius,0.6*wheel1_radius)
        self.second_wheel = Wheel(wheel2_center,wheel2_radius,0.6*wheel2_radius)
        wheel1_center.y-=rect_height
        self.top=Rectangle(wheel1_center,wheel2_center)
        wheel1_center.y+=rect_height/2
        wheel1_center.x-=rect_height
        wheel2_center.x+=rect_height
        self.body=Rectangle(wheel1_center,wheel2_center)
        
    def draw(self, win):
        self.top.draw(win)
        self.body.draw(win)
        self.first_wheel.draw(win)
        self.second_wheel.draw(win)
        
    def move(self, dx, dy):
        self.first_wheel.move(dx, dy)
        self.second_wheel.move(dx, dy)
        self.top.move(dx,dy)
        self.body.move(dx,dy)
    def set_color(self, wheel_color, tire_color,body):
        self.first_wheel.set_color(wheel_color, tire_color)
        self.second_wheel.set_color(wheel_color, tire_color)
        self.top.setFill(body)
        self.body.setFill(body)
        
    def undraw(self):
        self.tire_circle .undraw()
        self.wheel_circle .undraw()
    def get_size(self):
        return self.tire_circle.getRadius()
    def get_center(self):
        return self.tire_circle.getCenter()
    def animate(self, win, dx, dy, n):
        if n > 0:
            self.move(dx, dy)
            win.after(1000, self.animate, win, dx, dy, n-1)
# 1st wheel centered at 50,50 with radius 15
# 2nd wheel centered at 100,50 with radius 15
# rectangle with a height of 40
car1 = Car(Point(50, 50), 15, Point(100,50), 15, 40)
car1.draw( win )
# color the wheels grey with black tires, and the body pink
car1.set_color('black', 'grey', 'pink' )
# make the car move on the screen
car1.animate(win, 5, 0, 400)
win.mainloop()

