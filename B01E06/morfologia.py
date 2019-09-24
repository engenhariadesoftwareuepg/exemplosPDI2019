import cv2
import numpy as np

img = cv2.imread('../images/j.png',0)
#kernel = np.ones((5,5),np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
erosao = cv2.erode(img,kernel,iterations=1)
dilatacao = cv2.dilate(img, kernel,iterations=1 )
cv2.imshow("erosao",erosao)
cv2.imshow("dilatacao",dilatacao)
cv2.waitKey(0)