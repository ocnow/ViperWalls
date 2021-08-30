import cv2
import numpy as np

currMap = cv2.imread('map_shot.jpg')

res = cv2.Canny(currMap,100,200)

frmShape = res.shape
blank_image = np.zeros((frmShape[0],frmShape[1]), np.uint8)
blank_image1 = np.zeros((frmShape[0],frmShape[1]), np.uint8)
blank_image2 = np.zeros((frmShape[0],frmShape[1]), np.uint8)
blank_image3 = np.zeros((frmShape[0],frmShape[1]), np.uint8)
print(blank_image.shape)
print(frmShape)
#make every pixel after first white as black
for i in range(frmShape[0]):
    foundWhite = False
    for j in range(frmShape[1]):
        if foundWhite:
            blank_image[i][j] = 0
        elif res[i][j] != 0:
            blank_image[i][j] = 255
            foundWhite = True

for i in range(frmShape[0]):
    foundWhite = False
    for j in range(frmShape[1]-1,-1,-1):
        if foundWhite:
            blank_image1[i][j] = 0
        elif res[i][j] != 0:
            blank_image1[i][j] = 255
            foundWhite = True

#make every pixel after first white as black
for j in range(frmShape[1]):
    foundWhite = False
    for i in range(frmShape[0]):
        if foundWhite:
            blank_image2[i][j] = 0
        elif res[i][j] != 0:
            blank_image2[i][j] = 255
            foundWhite = True

for j in range(frmShape[1]):
    foundWhite = False
    for i in range(frmShape[0]-1,-1,-1):
        if foundWhite:
            blank_image3[i][j] = 0
        elif res[i][j] != 0:
            blank_image3[i][j] = 255
            foundWhite = True


res4 = cv2.bitwise_or(blank_image, blank_image1)
res4 = cv2.bitwise_or(res4, blank_image2)
res4 = cv2.bitwise_or(res4, blank_image3)

cv2.imshow('wind1',currMap)
cv2.imshow('wind2',res)
cv2.imshow('wind3',res4)

cv2.waitKey(0)
