import cv2
import numpy as np

currMap = cv2.imread('map_shot.jpg')

res = cv2.Canny(currMap,30,200)
frmShape = res.shape

itemindex = np.where(res == 255)


edge_pxls = []
ru = np.unique(itemindex[0])
for r in ru:
    wh = np.where(itemindex[0] == r)[0]
    edge_pxls.append((r,itemindex[1][wh[0]]))
    edge_pxls.append((r,itemindex[1][wh[-1]]))

blank_image = np.zeros((frmShape[0],frmShape[1]), np.uint8)
for pxl in edge_pxls:
    if(pxl[0] > 400):
        break
    for j in range(pxl[1],frmShape[1]):
        blank_image[pxl[0],j] = 255 - blank_image[pxl[0],j]

res4 = cv2.bitwise_and(currMap, currMap,mask = blank_image)
cv2.imshow('mask_image.jpg',res4)
#cv2.imwrite('mask_image.jpg',blank_image)
cv2.waitKey(0)
