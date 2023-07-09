import numpy as np
import cv2
import math

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
        rot_img = np.uint8(np.zeros((height_rot_img,width_rot_img,image.shape[2])))
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
                rot_img[i,j,:] = image[x,y,:]
    return rot_img 

def radon_transform(image, thetas, n):
    '''
    Computes Radon transform of image

    inputs: image: input image (dtype: numpy-ndarray)
    thetas: array containing angles of rotation
    n: size of image
    '''
    #n = image.shape[0]
    rt_img = np.uint8(np.zeros((image.shape[0],np.size(thetas),image.shape[2])))

    for th in range(np.size(thetas)):
        rot_img = naive_image_rotate(image,thetas[th]+90,'same')

        for i in range(n):
            Sum0 = (2/n)*sum(rot_img[i,:,0])
            Sum1 = (2/n)*sum(rot_img[i,:,1])
            Sum2 = (2/n)*sum(rot_img[i,:,2])

            rt_img[i,th,0] = Sum0
            rt_img[i,th,1] = Sum1
            rt_img[i,th,2] = Sum2

    return rt_img

def backproject(rt, thetas, n)
    '''
    Computes backprojection using sinogram of original image
    inputs: rt: input sinogram
    thetas: array containing angles of rotation
    n: size of image
    '''

if __name__=='__main__':
    #filename = 'mickey.png'
    rot_start = 0.01
    rot_end = 360
    steps = 256
    image = cv2.imread(r'/home/swuupii/ImageReconstruction/XRayTransform/mickey.png')
    n = image.shape[0]
    thetas = np.linspace(rot_start,rot_end,steps)
    
    rt = radon_transform(image,thetas,n)
    #print(image[:,32,:])
    #rotated_image = naive_image_rotate(image,30,'full')
    cv2.imshow("original image", image)
    cv2.imshow("sinogram",rt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()