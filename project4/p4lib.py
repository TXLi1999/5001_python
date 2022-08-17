'''
This is the library working for project 4. Functions includes drawing quadrant 1 - 4 and the frame.
Tuoxin Li 02/15/2022
'''

import turtle as t

#function to take turtle to a position without drawing 
#Retrived from Professor Gary's file
def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#reset the turtle to the home position and orientation
#Retrived from Professor Gary's file
def resetTurtle():
    t.penup()
    t.home()
    t.pendown()

def square(x,y,side):
    '''
    Function: square
    Params:3 floats.
    Return: draw a square given a position and length of a side
    '''
    goto(x,y)
    i = 0
    while i < 4:
        t.forward(side)
        t.left(90)
        i += 1


def frame(box_size):
    '''
    Function: frame
    Params:1 float.
    Return: create four boxes connected together based on a set size
    '''
    t.speed(0)
    square(-box_size/2,-box_size/2,box_size/2)
    square(0,-box_size/2,box_size/2)
    square(-box_size/2,0,box_size/2)
    square(0,0,box_size/2)


def windowSlates(x,y, blockSize, length, width):
    '''
    Function: window slate
    params: 5 floats
    Return:create horizontal stripes across the screen
    '''
    while(True):   ## I tried different ways to complete the while loop, so this one looks complex 
        y += 1
        if y % width ==0 and (y/width)%2 !=0 :
            goto(x,y)
            times = 1
            while times <= width:
                t.forward(length)
                goto(x,y + times)
                times +=1
                if y + times >= blockSize:
                    break
        if y >= blockSize:
            break
'''
this is a test for the horizental stripes part
t.speed(0)
windowSlates(-200,0,200,200,20)
t.mainloop()
'''

def zebraStripes(x,y, blockSize, length, width):
    '''
    Function: zebra stripes
    params: 5 floats
    Return:create verticle stripes across the screen
    '''
    xPos=x+width
    yPos=y
    t.setheading(90)
    while xPos-x<blockSize:  ## I tried different ways to complete the while loop, and this one looks better
        goto(xPos,yPos)
        times = 1
        while times <= width:
            t.forward(length)
            goto(xPos+ times,y)
            times +=1
            if xPos+times > blockSize:
                break
        xPos += 2*width
        

def steps(x,y,blockSize, stepsize):
    '''
    Function: steps
    params: 4 floats
    Return:create a stair case going from the bottom left corner to the top right
    '''
    xPos=x
    yPos=y
    while(True):  ##draw the horizental part of the steps
        xPos +=stepsize
        yPos = xPos
        if (xPos +stepsize)-x <=blockSize:
            goto(xPos,yPos)
            t.forward(stepsize)
        elif (xPos +stepsize)-x > blockSize and xPos -x< blockSize:
            goto(xPos,yPos)
            t.forward(blockSize-xPos)
        elif xPos -x> blockSize:
            break
    t.setheading(90)
    xPos=x
    yPos=y
    while  (True):  ##draw the vertical part of the steps
        xPos += stepsize
        yPos= xPos-stepsize
        if (yPos +stepsize)-y <=blockSize:
            goto(xPos,yPos)
            t.forward(stepsize)
        elif (yPos + stepsize)-y > blockSize and xPos -y< blockSize:
            goto(xPos,yPos)
            t.forward(stepsize)
        elif yPos -y> blockSize:
            break
'''
This is a test for the step part
frame(400)
steps(0,0,200,70)
t.mainloop()
'''

def wallPaper(x,y,blockSize,radius):
    '''
    Function: wall paper
    params: 4 floats
    Return: create a wallpaper pattern of four interlocking circles
    '''
    xPos=x+radius
    yPos=y
    while yPos + 2*radius - y <=blockSize:
        while xPos + radius -x <=blockSize:
                goto(xPos,yPos)
                t.circle(radius)
                xPos += radius
        yPos+=radius
        xPos=x+radius
'''   
## This is a test for the wallpaper part
frame(400)
wallPaper(0,-200,200,23)
t.mainloop()
'''
#Retrived from Professor Gary's file
#The difference is that I added the sixth one, fill the screen with randon dquadrants
def menu():
    '''
    Function:menu
    Return:print menu
    '''
    print("1. Fill quadrant top left with verticle bars")
    print("2. Fill quadrant top right with stripes")
    print("3. Fill quadrant bottom left with stairs")
    print("4. Fill quadrant bottom right with wallpaper pattern")
    print("5. Fill all quadrants")
    print("6. Fill the screen with randon dquadrants")
    print("7. Clear screen")
    print("8. Quit")

#choose which quadrant functions to call using boolean variables
#By calling the fill function, the windows will show the quadrant part which is called
def fill(quad1, quad2, quad3, quad4, window_size):
    if quad1 == 1:
        hwidth= float(input("Please enter horizental slate width : "))
        windowSlates(-window_size/2,0, window_size/2, window_size/2,hwidth)
        resetTurtle()

    if quad2 == 1:
        vwidth= float(input("Please enter vertical slate width : "))
        zebraStripes(0,0,window_size/2,window_size/2,vwidth)
        resetTurtle()

    if quad3 == 1:
        stepsize=float(input("Please enter step size : "))
        steps(-window_size/2,-window_size/2,window_size/2,stepsize)
        resetTurtle()

    if quad4 == 1:
        radius=float(input("Please enter radius : "))
        wallPaper(0,-window_size/2,window_size/2,radius)
        resetTurtle()
        
