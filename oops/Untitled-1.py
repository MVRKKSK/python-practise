
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 11:44:13 2022
@author: nitis
"""
import PIL
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import skimage
import cv2
from PIL import Image 
import numpy as np
from skimage import io, color
img = Image.open("images/madrid.jpg")
print(img)
print(img.format)
print(img.mode)
img1 = np.asarray(img)
print(type(img1))
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img = mpimg.imread("images/madrid.jpg")
print(type(img))
print(img)
print(img.shape)
plt.imshow(img)
plt.colorbar()
from skimage import io, img_as_float, img_as_ubyte
image_1 = io.imread("images/madrid.jpg")
image_2 = img_as_float(image_1)
import cv2
grey_img = cv2.imread("images/madrid.jpg", 0)
color_img = cv2.imread("images/madrid.jpg", 1)
print(type(grey_img))
print(type(color_img))
cv2.imshow("pic", grey_img)
cv2.imshow("color pic", color_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

