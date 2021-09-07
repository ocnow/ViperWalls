import cv2
import numpy as np


def getNumsCloser(num,arr):
    for i in range(len(arr)):
        if num < arr[i]:
            return (arr[i-1],arr[i])


def userInputCallback(event,x,y,flags,usrData):

    if event == cv2.EVENT_LBUTTONDOWN:
        mainImg  = whitenSquare(blank_image,whiteX,whiteY,x,y)
        cv2.imshow('maskour1',mainImg)
        cv2.imwrite('perrfect_mask.jpg',mainImg)

def makeRowWhite(img,rowNum,col,arrX,arrY):
    rind = np.where(arrX == rowNum)
    coll,colr = getNumsCloser(col,arrY[rind])
    print("found {0} {1}".format(coll,colr))
    for c in range(coll+1,colr):
        img[rowNum,c] = 0
    return img


def whitenSquare(img,arrX,arrY,col,row):
    rindx = np.where(arrY == col)
    rows = arrX[rindx]
    rt,rb = getNumsCloser(row,rows)
    for r in range(rt+1,rb):
        print("doing for {}".format(r))
        img1 = makeRowWhite(img,r,col,arrX,arrY)
    return img1

currMap = cv2.imread('map_shot.jpg')

res = cv2.Canny(currMap,30,200)
frmShape = res.shape

whiteX,whiteY = np.where(res == 255)
itemindex = (whiteX,whiteY)
edge_pxls = []
ru = np.unique(itemindex[0])
for r in ru:
    wh = np.where(itemindex[0] == r)[0]
    edge_pxls.append((r,itemindex[1][wh[0]]))
    edge_pxls.append((r,itemindex[1][wh[-1]]))

new_img = res.copy()
blank_image = np.zeros((frmShape[0],frmShape[1]), np.uint8)
for pxl in edge_pxls:
    if(pxl[0] > 400):
        break
    for j in range(pxl[1],frmShape[1]):
        blank_image[pxl[0],j] = 255 - blank_image[pxl[0],j]

res4 = cv2.bitwise_and(currMap, currMap,mask = blank_image)
#cv2.imwrite('mask_image.jpg',blank_image)

cv2.imshow('mask_image.jpg',res4)
cv2.setMouseCallback('mask_image.jpg',userInputCallback)
cv2.imshow('maskour',blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

