import cv2
import numpy as np


def negativo(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_GRAYSCALE)
    linhas, colunas = img.shape
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            negativo = 255 - img.item(i, j)
            img.itemset((i, j), negativo)

    cv2.imshow('Negativo', img)
    cv2.imwrite('resultados/imagem_negativo_gray.jpg', img)

def alterar(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_GRAYSCALE)
    linhas, colunas = img.shape
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            if img.item(i, j)<100:
                img.itemset((i, j), 0)
            elif img.item(i, j)>200:
                img.itemset((i, j), 255)

    cv2.imshow('Alterada', img)


def salvarJpgPng(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite('resultados/imagemJpg_gray.jpg', img)
    cv2.imwrite('resultados/imagemPng_gray.png', img)

def diferenca():
    imgJpg = cv2.imread('resultados/imagemJpg_gray.jpg', cv2.IMREAD_GRAYSCALE)
    imgPng = cv2.imread('resultados/imagemPng_gray.png', cv2.IMREAD_GRAYSCALE)
    linhasJpg, colunasJpg = imgJpg.shape
    linhasPng, colunasPng = imgPng.shape
    if linhasJpg!=linhasPng or colunasJpg!=colunasPng:
        print("Linhas ou colunas incompativeis")
        return
    diferenca = imgJpg.copy()
    for i in range(0, linhasJpg):
        for j in range(0, colunasJpg):
            diferenca.itemset((i, j), abs(imgJpg.item(i, j)-imgPng.item(i, j)))
    cv2.imshow('diferenca', diferenca)

def invertida(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_GRAYSCALE)
    invertida = img.copy()
    linhas, colunas = img.shape
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            invertida.itemset((i, j), img.item(linhas-i-1, colunas-j-1))

    cv2.imshow('Invertida', invertida)
    cv2.imwrite('resultados/imagem_invertida_gray.jpg', invertida)

def negativoColor(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_COLOR)
    print(img.shape)
    linhas, colunas, cores = img.shape
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            for k in range(0, cores):
                negativo = 255 - img.item(i, j, k)
                img.itemset((i, j, k), negativo)
                
    cv2.imshow('Negativo colorida', img)
    cv2.imwrite('resultados/imagem_negativo_color.jpg', img)


negativo('../images/shark.jpg')
alterar('../images/shark.jpg')
salvarJpgPng('../images/shark.jpg')
diferenca()
invertida('../images/shark.jpg')
negativoColor('../images/shark.jpg')
cv2.waitKey(0)
cv2.destroyAllWindows()

