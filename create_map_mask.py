import cv2
import numpy as np
import youtube_dl

img = cv2.imread('images/breeze_map/new_pre_mask.jpg')

print(img.shape)
cv2.imshow("Original", img)
cv2.waitKey(0)
