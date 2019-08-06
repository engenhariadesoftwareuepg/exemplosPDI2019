#Importar a bliblioteca do opencv
import cv2 as cv

#Leitura de uma imagem
# Opcoes de leitura da image
# - cv.IMREAD_COLOR
# - cv.IMREAD_GRAYSCALE
# - cv.IMREAD_UNCHANGED
imagem = cv.imread('../images/shark.jpg', cv.IMREAD_GRAYSCALE)

#mostrar imagem em uma janela
cv.imshow("Minha imagem", imagem)

#Esperar que alguma tecla seja precionada
cv.waitKey(0)
cv.destroyAllWindows()
