from graphics import *
'''
# create a window with width = 700 and height = 500
win = GraphWin('Program Name', 700, 500)
tri = Polygon(Point(0,500),Point(350,0), Point(700,500))
tri.setFill('yellow')
tri.draw(win)
win.mainloop() '''

def Sierpinski(level,point_b,point_a,point_c):
    colors=['yellow','green','blue','red','orange','purple','white','black','pink']
    tri = Polygon(point_b,point_a,point_c)
    l=level
    #for i in range(len(colors)):
    tri.setFill(colors[level%len(colors)])
    tri.draw(win)
    b_x=(point_c.x+point_b.x)/2.0
    b_y=point_b.y
    a_x=(point_a.x+point_b.x)/2.0
    a_y=(point_b.y+point_a.y)/2.0
    c_x=(point_c.x-point_a.x)/2.0+point_a.x
    c_y=(point_c.y+point_a.y)/2.0
    
    '''
    b1_x=( b_x-point_b.x)/2.0
    b1_y=(point_b.y)
    a1_x=(b_x-point_b.x)/2.0
    a1_y=(point_b.y-b_y)/2.0
    c1_x=(b_x-a_x)/2
    c1_y=(b_y-a_y)/2
    
    
    tri = Polygon(Point(b_x,b_y),Point(a_x,a_y),Point(c_x,c_y))
    print Point(b_x,b_y),Point(a_x,a_y),Point(c_x,c_y)
    tri.setFill('black')
    tri.draw(win)

    tri = Polygon(Point(b1_x,b1_y),Point(a1_x,a1_y),Point(c1_x,c1_y))
    print Point(b1_x,b1_y),Point(a1_x,a1_y),Point(c1_x,c1_y)
    tri.setFill('black')
    tri.draw(win)'''
   
    for i in range(1,level):
        Sierpinski(i,point_b,Point(a_x,a_y),Point(b_x,b_y))
        Sierpinski(i,Point(a_x,a_y),point_a,Point(c_x,c_y))
        Sierpinski(i,Point(b_x,b_y),Point(c_x,c_y),point_c)

#def half(point):
    
win = GraphWin('Program Name', 700, 500)
Sierpinski(50,Point(0,500),Point(350,0), Point(700,500))
win.mainloop()
