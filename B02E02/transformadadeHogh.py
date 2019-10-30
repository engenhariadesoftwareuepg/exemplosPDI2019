import cv2
import numpy as np

imagem = cv2.imread('../images/sodoku.jpg')
cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
arestas = cv2.Canny(cinza,50,50,apertureSize = 3)

lines = cv2.HoughLines(arestas,1,np.pi/180,165)
for l in lines:
    for rho,theta in l:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(imagem,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('Canny', arestas)
cv2.imshow('Transformada de Hough', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()