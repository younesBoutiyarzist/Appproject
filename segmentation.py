import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
from pylab import *

# Récupération de l'image 
Image = cv2.imread("./assets/fuwa_glace.png")
Image = cv2.resize(Image, (int(Image.shape[1]/3), int(Image.shape[0]/3)))
image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)
img=np.array(image,dtype=np.float64) 


IniLSF = np.ones((img.shape[0],img.shape[1]),img.dtype) 
IniLSF[30:80,30:80]= -1 
IniLSF=-IniLSF 


Image = cv2.cvtColor(Image,cv2.COLOR_BGR2RGB) 
plt.figure(1),plt.imshow(Image),plt.xticks([]), plt.yticks([])   # to hide tick values on X and Y axis
plt.contour(IniLSF,[0],color = 'b',linewidth=2)  
plt.draw(),plt.show(block=False) 

def mat_math (intput,str):
    output=intput 
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if str=="atan":
                output[i,j] = math.atan(intput[i,j]) 
            if str=="sqrt":
                output[i,j] = math.sqrt(intput[i,j]) 
    return output 


def CV (LSF, img, mu, nu, epison,step):

    Drc = (epison / math.pi) / (epison*epison+ LSF*LSF)
    Hea = 0.5*(1 + (2 / math.pi)*mat_math(LSF/epison,"atan")) 
    Iy, Ix = np.gradient(LSF) 
    s = mat_math(Ix*Ix+Iy*Iy,"sqrt") 
    Nx = Ix / (s+0.000001) 
    Ny = Iy / (s+0.000001) 
    Mxx,Nxx =np.gradient(Nx) 
    Nyy,Myy =np.gradient(Ny) 
    cur = Nxx + Nyy 
    Length = nu*Drc*cur 

    Lap = cv2.Laplacian(LSF,-1) 
    Penalty = mu*(Lap - cur) 

    s1=Hea*img 
    s2=(1-Hea)*img 
    s3=1-Hea 
    C1 = s1.sum()/ Hea.sum() 
    C2 = s2.sum()/ s3.sum() 
    CVterm = Drc*(-1 * (img - C1)*(img - C1) + 1 * (img - C2)*(img - C2)) 

    LSF = LSF + step*(Length + Penalty + CVterm) 
    #plt.imshow(s, cmap ='gray'),plt.show() 
    return LSF 


mu = 1 
nu = 0.003 * 255 * 255 
num =  5
epison = 1 
step = 0.1 
LSF=IniLSF 
for i in range(1,num):
    LSF = CV(LSF, img, mu, nu, epison,step) 
    if i == 3:   
        plt.imshow(Image),plt.xticks([]), plt.yticks([])  
        plt.contour(LSF,[0],colors='r',linewidth=2) 
        plt.draw(),plt.show(block=False),plt.pause(0.01) 

cv2.imshow("Avatar", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
"""import cv2

# read the image
image = cv2.imread('./assets/fuwa_glace.png')
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# visualize the binary image
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)
cv2.imwrite('image_thres1.jpg', thresh)
cv2.destroyAllWindows()
# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
                                      
# draw contours on the original image
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
                
# see the results
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()
"""
"""from PIL import Image
from numpy import asarray

import matplotlib.pyplot as plt
import numpy as np

image = Image.open('./assets/fuwa_glace.png').convert('L')
data = asarray(image)

from skimage import  segmentation
from skimage import filters
import matplotlib.pyplot as plt
import numpy as np

coins = data
mask = coins > filters.threshold_otsu(coins)
clean_border = segmentation.clear_border(mask).astype(np.int)

coins_edges = segmentation.mark_boundaries(coins, clean_border)

plt.figure(figsize=(8, 3.5))
plt.subplot(121)
plt.imshow(clean_border, cmap='gray')
plt.axis('off')
plt.subplot(122)
plt.imshow(coins_edges)
plt.axis('off')

plt.tight_layout()
plt.show()"""