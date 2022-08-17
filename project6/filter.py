'''
    Tuoxin Li
    filter.py
    This is the library working for the main doc of the project6, and its function is to swap or change pixels
    3/4/22
    CS5003
'''
# required imports
import graphicsPlus as gp


def swapRedBlue(image) :
    '''
    Function: swapRedBlue()
    Params: an image object
    Return: nothing
    '''
    # for each row i in the image
    for i in range(image.getWidth()): 
        # for each column j in the image
        for j in range(image.getHeight()): 
            # assign to (r, g, b) the pixel values at (j, i)
            # set the pixel indexed by (j, i)  to the value (b, g, r)
            #original pixel values
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #red blue swap pixel
            image.setPixel(i, j, gp.color_rgb(og_pixel_b, og_pixel_g, og_pixel_r))

def swapRedGreen(image) :
    '''
    Function: swapRedGreen()
    Params: an image object
    Return: nothing
    '''
    # for each row i in the image
    for i in range(image.getWidth()): 
        # for each column j in the image
        for j in range(image.getHeight()): 
            # assign to (r, g, b) the pixel values at (j, i)
            # set the pixel indexed by (j, i)  to the value (b, g, r)
            #original pixel values
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #red green swap pixel
            image.setPixel(i, j, gp.color_rgb(og_pixel_g, og_pixel_r, og_pixel_b))

def swapGreenBlue(image) :
    '''
    Function: swapGreenBlue()
    Params: an image object
    Return: nothing
    '''
    # for each row i in the image
    for i in range(image.getWidth()): 
        # for each column j in the image
        for j in range(image.getHeight()): 
            # assign to (r, g, b) the pixel values at (j, i)
            # set the pixel indexed by (j, i)  to the value (b, g, r)
            #original pixel values
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #green blue swap pixel
            image.setPixel(i, j, gp.color_rgb(og_pixel_r, og_pixel_b, og_pixel_g))
    
def brighten(image) :
    '''
    Function: brighten()
    Params: an image object
    Return: nothing
    '''
    # for each row i in the image
    for i in range(image.getWidth()): 
        # for each column j in the image
        for j in range(image.getHeight()): 
            # assign to (r, g, b) the pixel values at (j, i)
            # set the pixel indexed by (j, i)  to the value (b, g, r)
            #original pixel values
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #make all the RGB of the pixel larger, but not more than 255
            if og_pixel_r <= 205:
                og_pixel_r+=50
            else:
                og_pixel_r=255
            if og_pixel_g <= 205:
                og_pixel_g+=50
            else:
                  og_pixel_g=255
            if og_pixel_b <= 205:
                og_pixel_b+=50
            else:
                og_pixel_b=255
            #Set new pixel
            image.setPixel(i, j, gp.color_rgb(og_pixel_r, og_pixel_g, og_pixel_b))
        
def darken(image) :
    '''
    Function: darken()
    Params: an image object
    Return: nothing
    '''
    # for each row i in the image
    for i in range(image.getWidth()): 
        # for each column j in the image
        for j in range(image.getHeight()): 
            # assign to (r, g, b) the pixel values at (j, i)
            # set the pixel indexed by (j, i)  to the value (b, g, r)
            #original pixel values
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #make all the RGB of the pixel smaller, but not less than 0
            if og_pixel_r >= 50:
                og_pixel_r-=50
            else:
                og_pixel_r=0
            if og_pixel_g >= 50:
                og_pixel_g-=50
            else:
                  og_pixel_g=0
            if og_pixel_b >= 50:
                og_pixel_b-=50
            else:
                og_pixel_b=0
            image.setPixel(i, j, gp.color_rgb(og_pixel_r, og_pixel_g, og_pixel_b))

def nored(image) :
    '''
    Function: nored()
    Params: an image object
    Return: nothing
    '''
    # for each row i in the image
    for i in range(image.getWidth()): 
        # for each column j in the image
        for j in range(image.getHeight()): 
            # assign to (r, g, b) the pixel values at (j, i)
            # set the pixel indexed by (j, i)  to the value (b, g, r)
            #original pixel values

            og_pixel_g = image.getPixel(i,j)[1]
            og_pixel_b = image.getPixel(i,j)[2]
            #set red 0
            image.setPixel(i, j, gp.color_rgb(0, og_pixel_g, og_pixel_b))

def nogreen(image) :
    '''
    Function: nogreen()
    Params: an image object
    Return: nothing
    '''
    # for each row i in the image
    for i in range(image.getWidth()): 
        # for each column j in the image
        for j in range(image.getHeight()): 
            # assign to (r, g, b) the pixel values at (j, i)
            # set the pixel indexed by (j, i)  to the value (b, g, r)
            #original pixel values
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_b = image.getPixel(i,j)[2]
            #set green 0
            image.setPixel(i, j, gp.color_rgb(og_pixel_r, 0, og_pixel_b))

def noblue(image) :
    '''
    Function: swapRedGreen()
    Params: an image object
    Return: nothing
    '''
    # for each row i in the image
    for i in range(image.getWidth()): 
        # for each column j in the image
        for j in range(image.getHeight()): 
            # assign to (r, g, b) the pixel values at (j, i)
            # set the pixel indexed by (j, i)  to the value (b, g, r)
            #original pixel values
            og_pixel_r = image.getPixel(i,j)[0]
            og_pixel_g = image.getPixel(i,j)[1]

            #set blue 0
            image.setPixel(i, j, gp.color_rgb(og_pixel_r, og_pixel_g, 0))