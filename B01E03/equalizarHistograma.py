import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/shark.jpg', cv2.IMREAD_GRAYSCALE)

equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imshow("Comparar imagem equalizada", res)
cv2.waitKey(0)
cv2.destroyAllWindows()