import cv2
import numpy as np


def negativo(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_COLOR)
    linhas, colunas, canais = img.shape
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            for k in range(0, canais):
                negativo = 255 - img.item(i, j, k)
                img.itemset((i, j, k), negativo)

    cv2.imshow('Negativo', img)
    cv2.imwrite('resultados/imagem_negativo_color.jpg', img)

def alterar(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_COLOR)
    linhas, colunas, canais = img.shape
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            for k in range(0, canais):
                if img.item(i, j, k)<100:
                    img.itemset((i, j, k), 0)
                elif img.item(i, j, k)>200:
                    img.itemset((i, j, k), 255)

    cv2.imshow('Alterada', img)


def salvarJpgPng(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_COLOR)
    cv2.imwrite('resultados/imagemJpg_color.jpg', img)
    cv2.imwrite('resultados/imagemPng_color.png', img)

def diferenca():
    imgJpg = cv2.imread('resultados/imagemJpg_color.jpg', cv2.IMREAD_COLOR)
    imgPng = cv2.imread('resultados/imagemPng_color.png', cv2.IMREAD_COLOR)
    linhasJpg, colunasJpg, canaisJpg = imgJpg.shape
    linhasPng, colunasPng, canaisPng = imgPng.shape
    if linhasJpg!=linhasPng or colunasJpg!=colunasPng or canaisJpg!=canaisPng:
        print("Linhas ou colunas ou canais incompativeis")
        return
    diferenca = imgJpg.copy()
    for i in range(0, int(linhasJpg)):
        for j in range(0, colunasJpg):
            for k in range(0, canaisJpg):
                diferenca.itemset((i, j, k), abs(imgJpg.item(i, j, k)-imgPng.item(i, j, k)))

    cv2.imshow('diferenca', diferenca)

def invertida(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_COLOR)
    invertida = img.copy()
    linhas, colunas, canais = img.shape
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            for k in range(0, canais):
                invertida.itemset((i, j, k), img.item(linhas-i-1, colunas-j-1, k))

    cv2.imshow('Invertida', invertida)
    cv2.imwrite('resultados/imagem_invertida_color.jpg', invertida)

negativo('../images/shark.jpg')
alterar('../images/shark.jpg')
salvarJpgPng('../images/shark.jpg')
diferenca()
invertida('../images/shark.jpg')
cv2.waitKey(0)
cv2.destroyAllWindows()

