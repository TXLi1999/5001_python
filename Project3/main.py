'''
Edited by Tuoxin Li on 02/08/2022
This project draws two scenes about Maine, and most of the functions are from the shape library based on turtle 
'''

import shapelib as s
import turtle as t
def test1():
    ###This function is for testing the aggregate shapes in the library
    #s.draw_arc(-100,0,50,180,0)
    #s.block(-100,-100,50,100,True)
    #s.draw_angle(-200,-50.60,50)
    #s.draw_window(50,50,20,20)
    s.draw_circle(50,50,50)

##test1()
##t.mainloop()
##From the results, all the functions run well

def test2():
    ###This function is for testing the complex things in the library
    #s.house(0,0,1)
    s.husky(350,0,1)
##test2()
##t.mainloop()
##From the results, all the functions run well

def scene1():
    '''
    this function draws a small house and a large house. A husky logo is printed on the roof of the large house.    
    '''
    t.speed(0) ## set speed as fastest
    s.house(-150,0,0.5)  ## draw the small hosue
    s.house(0,0,1)  ## draw the large house
    s.husky(120,160,0.2) ## husky logo
    
    
scene1()
t.mainloop() 

def scene2():
    '''
    this function draws a house with a husky chimney and its reverse.
    '''
    t.speed(0)
    s.house(-180,0,1.2) ## draw the upside house
    s.husky(50,232,0.2) ## draw the husky chimney
    s.house(210,0,-1.4) ##draw the downside house
    t.mainloop()

scene2()
t.mainloop() 

