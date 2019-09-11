import numpy as np
import cv2

cap = cv2.VideoCapture(0)
laplaciano = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #canny = cv2.Canny(gray,100,200)
	
    opencvOutput = cv2.filter2D(gray, -1, laplaciano)
    cv2.imshow('frame',opencvOutput)
    cv2.imshow('camera',gray)
    tecla = cv2.waitKey(1)
    if tecla == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
