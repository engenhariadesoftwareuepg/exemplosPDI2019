#Importar a bliblioteca do opencv
import cv2 as cv
#Leitura de uma imagem
# Opcoes de leitura da image
# - cv.IMREAD_COLOR
# - cv.IMREAD_GRAYSCALE
# - cv.IMREAD_UNCHANGED
imagem = cv.imread('../images/shark.jpg', cv.IMREAD_GRAYSCALE)

#Copiar a imagem
img2 = imagem.copy()

#acessar o pixel na posicao 100,100
pixel = imagem[100, 100]
#ou
imagem.item(100, 100)

#setar o pixel na posicao 100,100 com o valor 42
imagem.itemset((100, 100), 42)

#escrever a dimensao da imagem em pixels (linhas x colunas)
print(imagem.shape)

#pegar o retorno da funcao e atribuir em variaveis linhas e colunas
linhas, colunas = imagem.shape
print(linhas)
print(colunas)

#percorrer a imagem com o laco for
for i in range(0, linhas):
	for j in range(0, int(colunas/2)):
		negativo = 255-imagem.item(i, j)
		imagem.itemset((i, j), negativo)


#mostrar a imagem na tela
cv.imshow("Minha imagem", imagem)

#esperar que a tecla ESC seja precionada
tecla=0
while tecla!=27:
    tecla = cv.waitKey(0)
#codigo da tecla ESC=27


cv.destroyAllWindows()
