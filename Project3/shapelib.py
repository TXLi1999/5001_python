'''
Edited by Tuoxin Li 02/07/2022
This is a library using turtle to create some simple structures like circle, block, triangle, arc; also, it includess two complex structures including husky and house.
'''

from tkinter import mainloop
import turtle

def goto(x = 0, y = 0):
    ''' Function: goto
        Params: four floats
        Return: send the turtle ot (x,y) without drawing the line
    '''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_line(x,y, length, heading):
    '''
    Function:draw a line
    parames: four floats
    Return: a straight line at the specified location of the specified length and needed heading
    '''
    goto(x,y)
    turtle.setheading(heading)
    turtle.forward(length)

def block(x, y, width, height,boolean =False):
    ''' Function: block
        Params: four floats, , and boolean for either True or false.
        Return: draw a block at the specified location of the specified size, also users can choose to fill the block by setting bollean as True
    '''
    goto(x, y)
    if (boolean == True):   ##if users put true, then fill the block with black
        turtle.pencolor("black")
        turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()
def draw_circle(x =0,y =0,radius =0):
    '''
    Function:draw circle
    params: three floats
    Return: draw a circle at the specified location with the specified radius
    '''
    goto(x,y)
    turtle.setheading(0)
    turtle.circle(radius)

def draw_angle(x, y, angle, length):
    '''
    Function: draw angle
    params: four floats
    return: draw an anle at the specified location with specified length and angle
    '''
    goto(x,y)
    turtle.setheading(90-angle/2)
    turtle.forward(length)
    turtle.right(180-angle)
    turtle.forward(length)

def draw_arc(x,y, radius, arc, heading =0):
    '''
    Function: draw arc
    params: 5 floats
    draw an anle at the specified location with specified radian and radius
    '''
    goto(x,y)
    turtle.setheading(heading)
    turtle.circle(radius,arc)

def draw_triangle(x,y, angle, length):
    '''
    Function: draw triangle
    params: four floats
    return: draw a black trianle at the specified location with specified length and angle
    '''
    goto(x,y)
    turtle.pencolor("black")
    turtle.begin_fill()
    turtle.setheading(90-angle/2)
    turtle.forward(length)
    turtle.right(180-angle)
    turtle.forward(length)
    turtle.end_fill()

def draw_window(x,y,width,height):
    '''
    Function: draw a window
    Params: 4 floaats
    Return:draw a window of a house with specified size at specified location
    '''
    block(x,y,width,height)
    draw_line(x+width/2 ,y, height, 90)
    draw_line(x ,y+height/2, width, 0)


def husky(x=0,y=0,scale=1):
    '''
    Function:husky
    params: 3 floats. scale can take from 0 - infinite(not including 0), and 1 is the normal size
    Return: draw a husky at specified location with specified size
    '''
    draw_arc(x,y+300*scale,300*scale,65,240)  ##draw face
    draw_arc(x+300*scale,y+300*scale,-300*scale,65,-60) ##draw face
    draw_angle(x,y+300*scale,60,50*(5**0.5)*scale) ##draw ears
    draw_triangle(x+10*scale,y+300*scale,60,92*scale) ##draw ears
    draw_angle(x+188*scale,y+300*scale,60,50*(5**0.5)*scale) ##draw ears
    draw_triangle(x+198*scale,y+300*scale,60,92*scale) ##draw ears
    draw_arc(x+188*scale,y+300*scale,60*scale,80,140) ##draw the top
    block(x+65*scale,y+200*scale,55*scale,30*scale,True) ##draw eyes
    block(x+180*scale,y+200*scale,55*scale,30*scale,True) ##draw eyes
    draw_circle(x+150*scale,y+130*scale,20*scale) ##draw nose
    draw_line(x+113*scale,y+93*scale,50*scale,-90) ##draw mouth
    draw_line(x+187*scale,y+93*scale,50*scale,-90) ##draw mouth
    draw_arc(x+113*scale,y+43*scale,37*scale,180,-90) ##draw mouth
    draw_arc(x+150*scale,y+130*scale,37*scale,180,-90) ##draw mouth
    draw_arc(x+76*scale,y+130*scale,37*scale,180,-90) ##draw mouth

def house(x =0,y =0,scale =1):
    '''
    Function:husky
    params: 3 floats. scale is 1 when it is the normal size
    Return: draw a husky at specified location with specified size
    '''
    block(x,y,300*scale,150*scale) ## wall
    draw_angle(x,y+150*scale,110,185*scale)  ## roof
    draw_window(x+50*scale,y+50*scale,60*scale,60*scale) ##window
    block(x+200*scale,y,60*scale,100*scale) ##door