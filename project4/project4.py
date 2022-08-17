'''
This file is based on p4lib, and works to draw 4 quadrants as the users wish
Edit by Tuoxin Li 02/17/2022
'''

import turtle as t
import p4lib as p
import random

def main():
    
    t.speed(0) #max out the speed    
    window_size = int(input("Please set window size : ")) #ask user to type the window size
    p.frame(window_size) #draw the asked windown
    
    while(True): #make an infinite loop for users to draw the quadrants
        p.menu() #print menu
        selection=int(input("Please make selection : "))  
        if selection ==1:  #if user types one, draw the horizental stripe graphic
            p.fill(1, 0, 0, 0, window_size)
        
        elif selection ==2: #if user types two, draw the vertical stripe graphic 
            p.fill(0, 1, 0, 0, window_size)
           
        elif selection ==3: #if user types three, draw the step graphic
            p.fill(0, 0, 1, 0, window_size)
           
        elif selection ==4: #if user types four, draw the circle graphic
            p.fill(0, 0, 0, 1, window_size)
       
        elif selection ==5: #if user types five, draw all the graphic
            p.fill(1, 1, 1, 1, window_size)
       
        elif selection ==6: #if user types six, draw the random graphic
            p.fill(round(random.random()), round(random.random()), round(random.random()), round(random.random()), window_size)
            
        elif selection ==7: #clear the screen if user types seven
            p.resetTurtle()
            t.clear()
            p.frame(window_size)
    
        elif selection == 8: #quit the turtle window if user types eight
           t.bye()
           break

main() 