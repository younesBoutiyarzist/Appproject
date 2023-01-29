import numpy as np
import cv2 

part = ['eye_R','eye_L','ear_R','ear_L','hat','mouth','moustache_R','moustache_L']

img_head = cv2.imread('partie/head.png', cv2.IMREAD_UNCHANGED) 
dimensions = img_head.shape
part_image = np.zeros((dimensions[0],dimensions[1]), np.uint8)
for i in range(len(part)):
    img = cv2.imread('./partie/mask' + part[i] + '.png') 
    # bloucler sur les pixel de l'image img_head
    for x in range (0,img.shape[0]):
        for y in range (0,img.shape[1]):
            # si le pixel est blanc
            if img[x,y,0] == 255 and img_head[x,y,3] != 0 :
                # on le remplace par le pixel de l'image img
                part_image[x,y] = 255
                img_head[x,y,:] = [255,255,255,255]
                
cv2.imwrite('./partie/mask.png',part_image)
cv2.imwrite('./partie/imageToImpaint.png',img_head)

img = cv2.imread('partie/imageToImpaint.png')
mask = cv2.imread('partie/mask.png', cv2.IMREAD_GRAYSCALE)
dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows