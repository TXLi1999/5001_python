'''
    Tuoxin Li
    Lab 6: Image
    Main work for project06
    warhol.py
    3/4/22
    CS5003
'''
# required imports
import graphicsPlus as gp
import sys
import filter


def main(argv) :
    if len(argv) >= 2:
        # read image data from a file and assign it to a variable
        src_image = gp.Image(gp.Point(0, 0), argv[1])
        # Creat new image based on the oringinal one in terms of doing the warhol work
        swaprb_image= gp.Image(gp.Point(0, 0), argv[1])
        swaprg_image= gp.Image(gp.Point(0, 0), argv[1])
        swapbg_image= gp.Image(gp.Point(0, 0), argv[1])
        brighten_image=gp.Image(gp.Point(0, 0), argv[1])
        darken_image=gp.Image(gp.Point(0, 0), argv[1])
        nored_image=gp.Image(gp.Point(0, 0), argv[1])
        nogreen_image=gp.Image(gp.Point(0, 0), argv[1])
        noblue_image=gp.Image(gp.Point(0, 0), argv[1])
        #Ask the user to input the name of the warhol work
        PicName=input("What the name of your warhol image? \n")
        # use getWidth() and getHeight() methods of the Image object to get its size
        width = src_image.getWidth()
        height = src_image.getHeight()
        #Put the title which is named by user at the middle of the whole work
        text0= gp.Text(gp.Point(1.5*width, 1.5*height),PicName)
        #Set the title yellow
        text0.setTextColor("yellow")
        #Front should be larger
        text0.setSize(35)
        #Set text for every single picture
        text1= gp.Text(gp.Point(1.5*width, 1.4*height),"Original")
        #Set the text white
        text1.setTextColor("white")
        text1.setSize(20)
        text2= gp.Text(gp.Point(0.5*width, 1.5*height),"Brighten")
        text2.setTextColor("white")
        text2.setSize(20)
        text3= gp.Text(gp.Point(2.5*width, 1.5*height),"Darken")
        text3.setTextColor("white")
        text3.setSize(20)
        text4= gp.Text(gp.Point(width/2, 0.5*height),"Swap Red and Blue")
        text4.setTextColor("white")
        text4.setSize(20)
        text5= gp.Text(gp.Point(1.5*width, 0.5*height),"Swap Red and Green")
        text5.setTextColor("white")
        text5.setSize(20)
        text6= gp.Text(gp.Point(2.5*width, 0.5*height),"Swap Green and Blue")
        text6.setTextColor("white")
        text6.setSize(20)
        text7= gp.Text(gp.Point(0.5*width, 2.5*height),"Lack red")
        text7.setTextColor("white")
        text7.setSize(20)
        text8= gp.Text(gp.Point(1.5*width, 2.5*height),"Lack green")
        text8.setTextColor("white")
        text8.setSize(20)
        text9= gp.Text(gp.Point(2.5*width, 2.5*height),"Lack blue")
        text9.setTextColor("white")
        text9.setSize(20)
        # create a GraphWin window to display the image
        window = gp.GraphWin("Image rendered", 3*width, 3*height)
        # move the image to the specified place
        src_image.move(1.5*width, 1.5*height)
        swaprb_image.move(0.5*width,0.5*height)
        swaprg_image.move(1.5*width,0.5*height)
        swapbg_image.move(2.5*width,0.5*height)
        brighten_image.move(0.5*width,1.5*height)
        darken_image.move(2.5*width,1.5*height)
        nored_image.move(0.5*width,2.5*height)
        nogreen_image.move(1.5*width,2.5*height)
        noblue_image.move(2.5*width,2.5*height)
        #Make swap or change pixels
        filter.swapRedBlue(swaprb_image) 
        filter.swapRedGreen(swaprg_image)
        filter.swapGreenBlue(swapbg_image)
        filter.brighten(brighten_image)
        filter.darken(darken_image)
        filter.nored(nored_image)
        filter.nogreen(nogreen_image)
        filter.noblue(noblue_image)
        # draw the image into the window
        src_image.draw(window)
        swaprb_image.draw(window)
        swapbg_image.draw(window)
        swaprg_image.draw(window)
        brighten_image.draw(window)
        darken_image.draw(window)
        nored_image.draw(window)
        noblue_image.draw(window)
        nogreen_image.draw(window)
        text0.draw(window)
        text1.draw(window)
        text2.draw(window)
        text3.draw(window)
        text4.draw(window)
        text5.draw(window)
        text6.draw(window)
        text7.draw(window)
        text8.draw(window)
        text9.draw(window)
        # wait for user input
        window.getMouse()

        
    else :
        print("Usage message")

# conditional call to main function
if __name__ == "__main__" :
    main(sys.argv)