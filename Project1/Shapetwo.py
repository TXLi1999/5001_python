'''
project one Shape two
This project is about using turtle library to draw my name TX with different scale
edited by Tuoxin Li 1/27/2021
'''


from turtle import*
scale=1.5
##make it black
colormode(255)
fillcolor(0,0,0)
begin_fill()
##draw TX
forward(140*scale) ##1
left(90)
forward(50*scale) ##2
left(90)
forward(330*scale) ##3
left(90)
forward(50*scale)  ##4
left(90)
forward(140*scale)  ##5
right(90)
forward(100*scale)  ##6
right(135)  ##left part
forward(120*scale)  ##7  
left(90)
forward(50*scale)   ##8
left(90)
forward(168*scale)  ##9
right(90)
forward(168*scale)  ##10
left(90)  
forward(50*scale)  ##11
left(90)
forward(120*scale)  ##12
right(135)  
forward(120*scale)  ##13
left(150)
forward(100*scale)  ##14
left(30)
forward(33.4*scale)  ##15
right(135)
forward(120*scale)  ##16 right part
left(90)
forward(50*scale)  ##17
left(90)
forward(168*scale)  ##18
right(90)
forward(168*scale)  ##19
left(90)
forward(50*scale)  ##20
left(90)
forward(120*scale)  ##21
right(135)
forward(100*scale)  ##22
right(90)
end_fill()


mainloop()  ##keep the graph