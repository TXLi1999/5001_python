'''
Base code for 5001 lab
Uses while loops to create shapes using turtle
9/28/2021
-Dr. G
'''

from ast import While
from os import times
from tkinter import mainloop
import turtle as t

#function to take turtle to a position without drawing 
#completed for you
def goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#reset the turtle to the home position and orientation
#completed for you
def resetTurtle():
    t.penup()
    t.home()
    t.pendown()

#draw a square given a position and length of a side
#use a while loop to reduce redundant lines of code
#remove the print statement
#To be completed in recitation
def square(x,y,side):
    goto(x,y)
    i = 0
    while i < 4:
        t.forward(side)
        t.left(90)
        i += 1



#create four boxes connected together based on a set size
#To be completed in recitation
def frame(box_size):
    i = 0
    goto(-box_size/2,-box_size/2)
    while i < 4:
        t.forward(box_size)
        t.left(90)
        i += 1

def window(box_size):
    t.speed(0)
    frame(box_size)
    square(-box_size/2,-box_size/2,box_size/2)
    square(0,-box_size/2,box_size/2)
    square(-box_size/2,0,box_size/2)
    square(0,0,box_size/2)

#create horizontal stripes across the screen
#To be completed in recitation
def windowSlates(x,y, blockSize, length, width):
    while(True):
        y += 1
        if y % width ==0 and (y/width)%2 !=0 :
            goto(x,y)
            times = 1
            while times <= width:
                t.forward(length)
                goto(x,y + times)
                times +=1
        if y >= blockSize:
            break
'''
t.speed(0)
windowSlates(-100,-100,200,200,20)
t.mainloop()
'''
#create verticle stripes across the screen (see the video)
#makes sure to stay within the lines
#to be completed indpendently
def zebraStripes(x,y, blockSize, length, width):
    t.speed(0)
    xPos=x+width
    yPos=y
    t.setheading(90)
    while xPos-x<blockSize:
        goto(xPos,yPos)
        times = 1
        while times <= width:
            t.forward(length)
            goto(xPos+ times,y)
            times +=1
        xPos += 2*width
        



#create a stair case going from the bottom left corner to the top right (see the video)
#to be completed indpendently 
def steps(x,y,blockSize, stepsize):
    xPos=x
    yPos=y
    while(True):
        xPos +=1
        if  xPos % stepsize ==0:  
            yPos = xPos
            goto(xPos,yPos)
            t.forward(stepsize)
        if xPos >= blockSize:
            break
    t.setheading(90)
    xPos=x
    yPos=y
    while(True):
        if yPos % stepsize ==0:
            xPos= yPos+ stepsize
            goto(xPos,yPos)
            t.forward(stepsize)
        yPos +=1
        if yPos >=blockSize:
            break

#create a wallpaper pattern of four interlocking circles (see the video)
#make sure to stay within the square
#to be completed indpendently
def wallPaper(x,y,blockSize,radius):
   
    xPos=x+radius
    yPos=y
    while(True):
        while(True):
            goto(xPos,yPos)
            t.circle(radius)
            xPos += radius
            if xPos >= blockSize:
                break
        yPos+=radius
        xPos=x+radius
        if yPos>=blockSize-radius:
            break


#print menu
#completed for you    
def menu():
    print("1. Fill quadrant top left with verticle bars")
    print("2. Fill quadrant top right with stripes")
    print("3. Fill quadrant bottom left with stairs")
    print("4. Fill quadrant bottom right with wallpaper pattern")
    print("5. Fill all quadrants")
    print("6. Clear screen")
    print("7. Quit")

#choose which quadrant functions to call using boolean variables
#TA's will help you with this partially
#Remove print statement
def fill(quad1, quad2, quad3, quad4, window_size):
    print("Fill function")

'''
#control flow starts here
def main():
    #max out the speed
    #t.speed(0)
 
    false_selection_count = 0
    
    window_size = int(input("Please set window size : "))
    window(window_size)
    while(True):
        #frame(window_size)
        menu()
        input1=input("something")

    #1. Draw a frame with four squares based on user input 
    #2. Setup an infinite while loop 
    #3. Inside this while loop print the menu and get the user selection
    #4. Call the fill method based on the user selection (don't implement the actual functions yet)
    #5. If the user selects 6, clear the screen and redraw the frame
    #6. If the user selects 7, close the turtle window and exit the while loop
    #7. Complete the quad1 fill as shown in the video (Task 7 image)

    ####### Independent Work #######
    #7. If the user enters an invalid number then just repeat the loop but increment the false selection counter. After 3 false attempts, terminate the program/
    #8. Implement each of the other menu items. See the video in the lab description for a demonstration of the program in action. 

    #NOTE: Make sure each fill stays within its quadrant
    #NOTE: You won't need t.done or t.mainloop
    #NOTE: Only ask for frame size once
    #NOTE: I've included some hints within each function call
    
main()
'''