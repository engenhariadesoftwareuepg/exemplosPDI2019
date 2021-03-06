
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import numpy as np
import cv2


image = cv2.imread('../images/moedas01.png')
shifted = cv2.pyrMeanShiftFiltering(image, 21, 51)
cv2.imshow("Original", image)
# Otsu's thresholding
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Thresh", thresh)

# utilizar a distância euclidiana
D = ndimage.distance_transform_edt(thresh)
localMax = peak_local_max(D, indices=False, min_distance=20,
	labels=thresh)

# usar os vizinhos 8 conectados para aplicar o algoritmo Watershed
markers = ndimage.label(localMax, structure=np.ones((3, 3)))[0]
labels = watershed(-D, markers, mask=thresh)
print("[INFO] {} segmentos unicos econtrados".format(len(np.unique(labels)) - 1))

# loop sobre os segmentos encontrados
for label in np.unique(labels):
	# se for 0 é o fundo
	if label == 0:
		continue

	mask = np.zeros(gray.shape, dtype="uint8")
	mask[labels == label] = 255

	# Detectar os contornos
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	c = max(cnts, key=cv2.contourArea)

	# desenhar um circulo
	((x, y), r) = cv2.minEnclosingCircle(c)
	cv2.circle(image, (int(x), int(y)), int(r), (0, 255, 0), 2)
	cv2.putText(image, "#{}".format(label), (int(x) - 10, int(y)),
		cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# mostrar a imagem
cv2.imshow("Resultado", image)
cv2.waitKey(0)