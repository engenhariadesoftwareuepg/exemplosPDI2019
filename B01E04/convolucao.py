# Importar as bibliotecas necessarias
import numpy as np
import cv2
# Antes instalar a biblioteca scikit-image
# pip install scikit-image
from skimage.exposure import rescale_intensity

def convolve(image, filtro):
	#Pegar as dimensoes da imagem e do filtro
    imgLinhas, imgColunas = image.shape
    kLinhas, kColunas = filtro.shape
	# Calcula o deslocamento da mascara, ou seja metade inteira do numero de colunas
    pad = (kColunas - 1) // 2
    #Faz uma copia da imagem aumentando-a no valor do pad pixels, replicando o pixel
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad, cv2.BORDER_REPLICATE)
    #cria a imagem de saida com o valor 0 em todas as posicoes
    output = np.zeros((imgLinhas, imgColunas), dtype="float32")

	# Faz um laco, ignorando a borda para percorrer a imagem
    for y in np.arange(pad, imgLinhas + pad):
        for x in np.arange(pad, imgColunas + pad):
			#pega a subimagem de pixels vizinhos do tamanho do filtro
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

			#Multiplica pelo filtro e soma a matriz
            k = (roi * filtro).sum()

			# armazena na imagem de retorno (lembrando que na imagem original agora temos uma borda y-pad e x-pad)
            output[y - pad, x - pad] = k

	# pode ser que os valores saiam fora da escala, entao vamos colocar na escala de 0 ate 255
    output = rescale_intensity(output, in_range=(0, 255))
    output = (output * 255).astype("uint8")

	# retorna a imagem
    return output


# Utilizar um filtro para mascara de media de 7x7 e 21x21 pixels
borrarPouco = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
borrarMuito = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))

# Filtro de nitidez
nitidez = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")

# Filtro laplaciano para detectar cantos
laplaciano = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")

# Filtro sobel sobre o eixo x
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")

# filtro sobel sobre o eixo y
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")

# Contruir um banco de filtros para exibir todos em um loop
todosFiltros = (
	("Borrar pouco", borrarPouco),
	("Borrar muito", borrarMuito),
	("nitidez", nitidez),
	("laplaciano", laplaciano),
	("sobel_x", sobelX),
	("sobel_y", sobelY)
)

# carregar a imagem e converter na escala de cinza
image = cv2.imread("../images/shark.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# loop sobre os filtros
for (nomeFiltro, filtro) in todosFiltros:
	# aplicar o filtro para a escala em ciza, utilizando a nossa funcao de convolucao
    # E a funcao filter2D do opencv (o resultado deve ser exatamente igual)
	print("Aplicando o filtro {}".format(nomeFiltro))
	convoleOutput = convolve(gray, filtro)
	opencvOutput = cv2.filter2D(gray, -1, filtro)

	# mostrar as imagens de saida
	cv2.imshow("original", gray)
	cv2.imshow("{} - convole".format(nomeFiltro), convoleOutput)
	cv2.imshow("{} - opencv".format(nomeFiltro), opencvOutput)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
