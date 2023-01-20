import numpy as np
import cv2 as cv

img = cv.imread('test/imageToImpaint.png')
mask = cv.imread('test/mask.png', cv.IMREAD_GRAYSCALE)
dst = cv.inpaint(img,mask,3,cv.INPAINT_TELEA)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()