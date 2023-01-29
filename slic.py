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

# load the image and convert it to a floating point data type
image = cv2.imread("./assets/fuwa_glace.png") 
# apply SLIC and extract (approximately) the supplied number
# of segments
img = slic(image, n_segments = 400, sigma = 5)

cv2.imwrite('seg.png', img)