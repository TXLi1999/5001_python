'''
project one extension
This project is about using turtle library to draw my name TX in different color
edited by Tuoxin Li 1/27/2021
'''
from turtle import*

scale=1.0
##make it black
colormode(255)
fillcolor(0,0,0)
begin_fill()
##draw T
forward(140*scale)
left(90)
forward(50*scale)
left(90)
forward(330*scale)
left(90)
forward(50*scale)
left(90)
forward(140*scale)
right(90)
forward((135.36+120+100)*scale)
left(150)
forward(100*scale)
left(30)
forward((135.36+120+100-86.5)*scale)
end_fill()
left(90)
forward(50*scale)
left(90)
forward(100*scale) 
fillcolor(255,0,0)
begin_fill()
right(135)  ## X left part
forward(120*scale)
left(90)
forward(50*scale)
left(90)
forward(168*scale)
right(90)
forward(168*scale)
left(90)
forward(50*scale)
left(90)
forward(120*scale)
end_fill()  
right(45)
forward(50*scale)
fillcolor(0,0,255)
begin_fill()
right(45)  ## X right part
forward(120*scale)
left(90)
forward(50*scale)
left(90)
forward(168*scale)
right(90)
forward(168*scale)
left(90)
forward(50*scale)
left(90)
forward(120*scale)
left(45)
forward(86.5*scale)
end_fill()


mainloop() ##keep the graph
