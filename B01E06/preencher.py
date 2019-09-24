import cv2
import numpy as np

img = cv2.imread('../images/j.png',0)
h, w = img.shape
mask = np.zeros((h + 2, w + 2), np.uint8)
#o ponto 22, 72 é um ponto dentro do j
cv2.floodFill(img, mask, (22, 72), 100);
cv2.imshow("jota",img)
#o ponto 75, 18 é um ponto dentro do pingo do j
cv2.floodFill(img, mask, (75, 18), 50);
cv2.imshow("Pingo",img)
cv2.waitKey(0)