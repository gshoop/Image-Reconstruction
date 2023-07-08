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

if __name__=='__main__':
    filename = "mickey.png"
    image = cv2.imread(filename)
    rotated_image = naive_image_rotate(image,30,'full')
    cv2.imshow("original image", image)
    cv2.imshow("rotated image",rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()