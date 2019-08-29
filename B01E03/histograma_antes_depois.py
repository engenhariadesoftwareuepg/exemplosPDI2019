import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/shark.jpg', cv2.IMREAD_GRAYSCALE)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
#plt.legend(('cdf','histogram'), loc = 'upper left')

equ = cv2.equalizeHist(img)
histe,binse = np.histogram(equ.flatten(),256,[0,256])

cdfe = histe.cumsum()
cdf_normalizede = cdfe * histe.max()/ cdfe.max()
plt.plot(cdf_normalizede, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'g')
plt.xlim([0,256])
plt.legend(('cdf', 'cdf equalizado', 'Histograma', 'Histograma equalizado'), loc = 'upper left')
plt.show()