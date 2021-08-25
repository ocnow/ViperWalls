import cv2
import numpy as np
import youtube_dl

img = cv2.imread('breeze_map.png')
#removing breeze title
img[0:90,792:1024,:] = [49,14,24]

#making mask by changing outer to black
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_shape = img_hsv.shape

new_img = [[0 for i in range(img_shape[0])]for j in range(img_shape[1])]
for i in range(img_shape[0]):
    for j in range(img_shape[1]):
        pxl = img_hsv[i][j]
        if pxl[0] == 129 and pxl[1] == 182 and pxl[2] == 49:
            new_img[i][j] = 0
        else:
            new_img[i][j] = 255

X_new = np.array(new_img, dtype=np.float32)
while True:
    cv2.imshow('map_img',X_new)
    #filename = 'breezeMapMask.jpg'
    #cv2.imwrite(filename, X_new)

    if cv2.waitKey(30)&0xFF == ord('q'):
        break
