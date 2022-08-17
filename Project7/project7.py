'''
CS5001 Project 7
Tuoxin Li
3/23/2022
'''

import turtle as t
import random

def goto(x,y):
    '''
    This function allows user to move the pen without drawing
    '''
    t.penup()
    t.goto(x,y)
    t.pendown()

def box(x,y,size):
    '''
    Function:draw a box with perticular size at specified location
    '''
    goto(x,y)

    for i in range(4):
        t.forward(size)
        t.left(90)

   
def boxes(x, y, size, scaleDown, min_size):
    '''
    Function: draw the boxes inside box at specified location
    Parameters: Size is the largest box's size, scaleDown is the proportion to zoom out the box. End when it reaches the min_size 
    '''
    # base case
    if(size <= min_size):
        return
    # draw first box 
    box(x, y, size)
    # recursive call
    boxes(x+.5*size*scaleDown, y+.5*size*scaleDown, size-(size*scaleDown), scaleDown, min_size)

def cir(x,y,radius):
    '''
    funtion:draw a circle with radius at specified location
    '''
    goto(x,y)
    t.circle(radius)

def circles(x,y,radius,scaleDown,min_radius):
    '''
    Function: draw the circles inside circle at specified location
    Parameters: radius is the largest circle's radius, scaleDown is the proportion to zoom out the circle. End when it reaches the min_radius 
    '''
    # base case
    if(radius<=min_radius):
        return
    #draw the first circle
    cir(x,y,radius)
    # recursive call
    circles(x,(y+scaleDown*radius),radius-(radius*scaleDown),scaleDown,min_radius)

def Spiral(linelen):
    '''
    Function: draw the spiral
    Parameters: linelen is the started line length
    every recursive line reduced by 5
    '''
    # base case
    if linelen<=0:
        return
    #draw the first line
    t.forward(linelen)
    t.right(90)
    # recursive call
    Spiral(linelen-5)

def drawSpiral(x,y,linelen):
    '''
    function: put the spiral at specified location
    '''
    goto(x,y)
    Spiral(linelen)


def boxTree(x,y,size,scaleDown,min_size):
    '''
    Function: draw a box tree
    parems: size is the largest box size, ends when it reaches the min_size
    '''
    # base case
    if size<min_size:
        return
    #draw the first box
    box(x,y,size)
    #recursive call, draw the left box
    boxTree(x-(size-size*scaleDown)*0.8,y+size,size-size*scaleDown,scaleDown,min_size)
    #recursive call, draw the right box
    boxTree(x+size-(size-size*scaleDown)*0.2,y+size,size-size*scaleDown,scaleDown,min_size)

def circleTree(x,y,radius,scaleDown,min_radius):
    '''
    Function: draw circles to fit the box tree
    '''
    #base case
    if radius<=min_radius:
        return
    #first circles
    circles(x,y,radius,scaleDown,min_radius)
    #recursive call, left circles
    circleTree(x-radius-(2*radius-2*radius*scaleDown)*0.8+radius*scaleDown,y+2*radius,radius-radius*scaleDown,scaleDown,min_radius)
    #recursive call, right circles
    circleTree(x+radius+(2*radius-2*radius*scaleDown)*0.8-radius*scaleDown,y+2*radius,radius-radius*scaleDown,scaleDown,min_radius)

def branch(type,color):
    '''
    function:draw a branch with leaves; the leave could be put at left or right or both sides.
    parems:type=1 to draw the leaf at right side; type=2 to draw the leaf at left side; type=3 to draw the leaf at both sides. color is for the leaves' color
    '''
    t.forward(50)
    t.back(30)
    #draw right leaf
    if type ==1 or type == 3:
        t.color(color)
        t.begin_fill()
        t.right(90)
        t.forward(20)
        t.left(45)
        t.forward(15)
        t.left(135)
        t.forward(20)
        t.left(45)
        t.forward(15)
        t.end_fill()
        t.color("black")
        t.right(135)
        t.forward(30)

    if type ==3:
        t.back(30)
    #draw left leaf
    if type ==2 or type == 3:
        t.color(color)
        t.begin_fill()
        t.left(90)
        t.forward(20)
        t.right(45)
        t.forward(15)
        t.right(135)
        t.forward(20)
        t.right(45)
        t.forward(15)
        t.end_fill()
        t.color("black")
        t.left(135)
        t.forward(30)

def tree(color,number):
    '''
    function:draw a tree with wanted branches and wanted colored leaves
    params: color is the color of the leaves, number is the number of the branches
    '''
    # base case
    if number<1:
        return
    #randomly draw the leaves at right or left or both side
    n = random. randint(1,3)
    #draw the first branch
    branch(n,color)
    t.left(30)
    #recursive call, draw the left branch
    tree(color,number-1)
    t.right(60)
    #recursive call, draw the right branch
    tree(color,number-1)
    t.left(30)
    t.backward(50)

def drawTree(x,y,color,number):
    '''
    function:flip the tree and put it at specified location
    '''
    goto(x,y)
    t.left(90)
    t.forward(80)
    tree(color,number)




def main():
    t.speed(0)
    #boxes(0,0,300,.25,5)
    #circles(0,0,150,.25,2)
    #drawSpiral(0,0,100)
    #boxTree(0,0,100,.50,25)
    #circleTree(50,0,50,.5,5) #Run the code with code line 195
    color=input("Choose the color for the leaves. (Green or yellow.)\n")
    drawTree(0,0,color,8)
    t. hideturtle() #Hide turtle
    t.mainloop()
    
main()
