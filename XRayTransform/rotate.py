import numpy as np
import cv2
import math
import matplotlib.pyplot as plt

def naive_image_rotate(image, degrees, option='same'):
    '''
    This function rotates the image around its center by amount of degrees
    provided. The rotated image can be of the same size as the original image
    or it can show the full image.
    
    inputs: image: input image (dtype: numpy-ndarray)
            degrees: amount of rotation in degrees (e.g., 45,90 etc.)
            option: string variable for type of rotation. It can take two values
            'same': the rotated image will have same size as the original image
                    It is default value for this variable.
            'full': the rotated image will show the full rotation of original
                    image thus the size may be different than original.
    '''
    # First we will convert the degrees into radians
    rads = math.radians(degrees)
    # Finding the center point of the original image
    cx, cy = (image.shape[1]//2, image.shape[0]//2)
    
    if(option!='same'):
        # Let us find the height and width of the rotated image
        height_rot_img = round(abs(image.shape[0]*math.sin(rads))) + \
                           round(abs(image.shape[1]*math.cos(rads)))
        width_rot_img = round(abs(image.shape[1]*math.cos(rads))) + \
                           round(abs(image.shape[0]*math.sin(rads)))
        rot_img = np.uint8(np.zeros((height_rot_img,width_rot_img)))
        # Finding the center point of rotated image.
        midx,midy = (width_rot_img//2, height_rot_img//2)
    else:
        rot_img = np.uint8(np.zeros(image.shape))
     
    for i in range(rot_img.shape[0]):
        for j in range(rot_img.shape[1]):
            if(option!='same'):
                x= (i-midx)*math.cos(rads)+(j-midy)*math.sin(rads)
                y= -(i-midx)*math.sin(rads)+(j-midy)*math.cos(rads)
                x=round(x)+cy
                y=round(y)+cx
            else:
                x= (i-cx)*math.cos(rads)+(j-cy)*math.sin(rads)
                y= -(i-cx)*math.sin(rads)+(j-cy)*math.cos(rads)
                x=round(x)+cx
                y=round(y)+cy

            if (x>=0 and y>=0 and x<image.shape[0] and  y<image.shape[1]):
                rot_img[i,j] = image[x,y]
    return rot_img 

def radon_transform(image, thetas, n):
    '''
    Computes Radon transform of image

    inputs: image: input image (dtype: numpy-ndarray)
            thetas: array containing angles of rotation
            n: size of image
    '''
    
    rt_img = np.uint8(np.zeros((image.shape[0],np.size(thetas))))

    for th in range(np.size(thetas)):
        rot_img = naive_image_rotate(image,thetas[th]+90,'same')

        for i in range(n):
            Sum0 = (2/n)*sum(rot_img[i,:])
            rt_img[n-1-i,th] = Sum0

    return rt_img

def backproject(rt, thetas, n):
    '''
    Computes backprojection using sinogram of original image
    inputs: rt: input sinogram (dtype: numpy-ndarray)
            thetas: array containing angles of rotation
            n: size of image
    '''

    img_recon = np.uint8(np.zeros((n,n)))
    temp = np.uint8(np.zeros((n,n)))
    

    for th in range(np.size(thetas)):
        for i in range(n):
            temp[i,:] = rt[:,th]

        temp = naive_image_rotate(temp,-thetas[th],'same')

        img_recon += temp                                   # Normalization needed
        # Need to take core of when pixel values overflow over 255

    return img_recon

    
    

if __name__=='__main__':

    rot_start = 0.01
    rot_end = 180
    steps = 100
    image = cv2.imread(r'/home/swuupii/ImageReconstruction/XRayTransform/mickey.png',0)
    n = image.shape[0]
    thetas = np.linspace(rot_start,rot_end,steps)   # Thetas in degrees since naive_image_rotation converts to rad
    
    # Point source example
    new_img = np.zeros((n,n))
    new_img[20,9] = 255

    # Perform radon_transform on original image then backproject the sinogram 'rt'
    rt = radon_transform(new_img,thetas,n)
    img = backproject(rt,thetas,n)

    plt.figure(1)
    plt.imshow(new_img,cmap='gray')

    plt.figure(2)
    plt.imshow(rt,cmap='gray')
    x_ticks = np.linspace(0, np.pi, 3)
    x_labels = ['0', 'π', '2π']
    plt.xticks(np.linspace(0, len(thetas), len(x_ticks)), x_labels)

    plt.figure(3)
    plt.imshow(img,cmap='gray')
    plt.show()

    #plt.figure(4)
    #plt.imshow(new_img,cmap='gray')
    #plt.show()