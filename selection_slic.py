# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt
import argparse
import cv2
import numpy as np
import random

imgori = cv2.imread('./assets/fuwa_glace.png', cv2.IMREAD_UNCHANGED) 
dimensions = imgori.shape
imgori = cv2.resize(imgori, (round(dimensions[0]/3), round(dimensions[1]/3))) 
print(imgori.shape)
img1 = cv2.imread('seg.png', cv2.IMREAD_UNCHANGED) 
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB) 
dimensions = img1.shape
img = cv2.resize(img1, (round(dimensions[0]/3), round(dimensions[1]/3))) 
# Create point matrix get coordinates of mouse click on image
point_matrix = np.zeros((2,2),np.int)
part = ['head','eye_R','eye_L','ear_R','ear_L','hat','mouth','moustache_R','moustache_L']
part_data = np.zeros((2,2, len(part)),np.int)
part_counter = 0
counter = 0


### selection  des parties  

 # font
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2


def mousePoints(event,x,y,flags,params):
    global counter
    global img
    global ter
    global part_image
    global part_image1
    # Left button mouse click event opencv
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix[counter] = x,y
        a = img == img[y,x]
        part_image[a[:,:,1],:] = [255, 255, 255]
        cv2.imwrite('./partie/mask' + part[part_counter] + '.png', part_image)
        print(a.shape)
        part_image1[a[:,:,1],:] = imgori[a[:,:,1],:]
        cv2.imwrite('./partie/' + part[part_counter] + '.png', part_image1)
        counter = 0

    if event == cv2.EVENT_RBUTTONDOWN:

        part_image = np.zeros((round(dimensions[0]/3), round(dimensions[1]/3),3), np.uint8)
        part_image1 = np.zeros((round(dimensions[0]/3), round(dimensions[1]/3),4), np.uint8)
        ter = 1

part_image = np.zeros((round(dimensions[0]/3), round(dimensions[1]/3),3), np.uint8)
part_image1 = np.zeros((round(dimensions[0]/3), round(dimensions[1]/3),4), np.uint8)

ter = 0
while True:
    for x in range (0,2):
        cv2.circle(img,(point_matrix[x][0],point_matrix[x][1]),3,(0,255,0),cv2.FILLED)
 
    
    img_n = cv2.putText(img, 'select ' + part[part_counter], org, font, fontScale, color, thickness, cv2.LINE_AA)

    # Showing original image
    cv2.imshow("Original Image ", img_n)
    
    # Mouse click event on original image
    cv2.setMouseCallback("Original Image ", mousePoints)
    # Printing updated point matrix
    # Refreshing window all time
    if ter == 1:
        part_counter = part_counter + 1
        img = cv2.resize(img1, (round(dimensions[0]/3), round(dimensions[1]/3))) 
        ter = 0

    cv2.waitKey(1)
cv2.destroyAllWindows()
