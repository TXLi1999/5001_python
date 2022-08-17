'''
This is designed as a conventer.
Edited by Tuoxin Li
2/3/2022
'''



from turtle import*
def dollar():
    ##name: ussing turtle drawing dollar logo
    ##parameter:none
    ##return:graph
    pencolor("orange")
    speed(0)
    left(180)
    forward(100)
    left(90)
    forward(80)
    left(90)
    forward(100)
    right(90)
    forward(80)
    right(90)
    forward(100)
    back(30)
    left(90)
    forward(60)
    back(280)
    forward(60)
    left(90)
    forward(40)
    left(90)
    forward(60)
    back(280)
    mainloop()

def bitcoin():
    ##name: ussing turtle drawing bitcoin logo
    ##parameter:none
    ##return:graph
    speed(0)
    fillcolor("white")
    begin_fill()
    circle(100,-390)
    end_fill()
    left(105)
    fillcolor("orange")
    begin_fill()
    forward(162)
    right(90)
    forward(50)
    right(45)
    forward(30)
    right(45)
    forward(30)
    right(45)
    forward(30)
    right(45)
    forward(40)
    back(40)
    left(135)
    forward(30)
    right(45)
    forward(30)
    right(45)
    forward(30)
    right(45)
    forward(50)
    end_fill()
    mainloop()
    forward(100)
    mainloop()

def eth():
    ##name: ussing turtle drawing ethereum logo
    ##parameter:none
    ##return:graph
    speed(0)
    colormode(255)
    pencolor(255,255,255)
    fillcolor((0,204,204))
    begin_fill()
    right(140)
    forward(100)
    left(160)
    forward(82)
    right(40)
    forward(82)
    left(160)
    forward(100)
    end_fill()
    fillcolor(0,153,153)
    begin_fill()
    back(100)
    left(60)
    forward(82)
    right(40)
    forward(82)
    right(140)
    forward(82)
    right(40)
    forward(82)
    end_fill()
    right(70)
    forward(20)
    fillcolor(0,200,200)
    begin_fill()
    right(70)
    forward(82)
    right(40)
    forward(82)
    left(140)
    forward(157)
    left(120)
    forward(157)
    end_fill()
    mainloop()

amount= int(input("Please enter a currency amount : "))
currency_in=int(input("Amount entered was in what form? \nEnter : \n1.USD  \n2.BitCoin \n3.Ethereum \n"))

set=[1,2,3]
if (currency_in in set) :
    print("")     
else:
    print("please enter 1, 2 or 3 to continue")
    currency_in=int(input("Amount entered was in what form? \nEnter : \n1.USD  \n2.BitCoin \n3.Ethereum \n"))

convernt_to=int(input("Convert the entered amount to what form? \nEnter: \n1. USD \n2. Bitcoin \n3. Ethereum \n"))
if (convernt_to in set) :
    print("")     
else:
    print("please enter 1, 2 or 3 to continue")
    convernt_to=int(input("Choose the correct number. \nEnter : \n1.USD  \n2.BitCoin \n3.Ethereum \n"))

if (currency_in==1 ):
    if (convernt_to==2):
        final_amount= amount/36904
    else:
        final_amount=amount/2651

if (currency_in==2 ):
    if (convernt_to==1):
        final_amount= amount*36904
    else:
        final_amount=amount*13.9

if (currency_in==3 ):
    if (convernt_to==1):
        final_amount= amount*2651
    else:
        final_amount=amount/13.9

if (currency_in== convernt_to):
    final_amount=amount

print("The convernted amount is ",final_amount)

if (convernt_to==1):
    dollar()

if (convernt_to==2):
    bitcoin()

if (convernt_to ==3):
    eth()