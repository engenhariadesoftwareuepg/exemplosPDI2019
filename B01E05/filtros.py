import cv2

img = cv2.imread('../images/shark.jpg', cv2.IMREAD_GRAYSCALE) # Carregar a imagem
img_mediana = cv2.medianBlur(img, 5) # aplicar o filtro mediana
img_gausiana = cv2.GaussianBlur(img,(5,5),0) #aplicar o filtro gausiano
cv2.imshow('Imagem Original', img) # Mostrar a imagem Original
cv2.imshow('Imgem Mediana', img_mediana) # Mostrar a imagem com o filtro mediana
cv2.imshow('Imagem Gausiana', img_gausiana) # Mostrar a imagem com o filtro mediana
cv2.waitKey(0)        # Aguardar uma tecla ser precionada
cv2.destroyAllWindows # fechar as janelas