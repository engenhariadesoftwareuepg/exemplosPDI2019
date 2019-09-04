import cv2
import numpy as np


def rotular(nomeImagem):
    img = cv2.imread(nomeImagem, cv2.IMREAD_GRAYSCALE)
    linhas, colunas = img.shape
    rotulo = 1
    objetos = 0
    equivalentes = [0 for x in range(256)]
    for i in range(0, int(linhas)):
        for j in range(0, int(colunas)):
            if img.item(i, j) != 0:
                if i == 0:
                    r = 0
                else:
                    r = img.item(i-1, j)
                if j == 0:
                    t = 0
                else:
                    t = img.item(i, j-1)
                if r == 0 and t == 0:
                    img.itemset((i, j), rotulo)
                    rotulo += 1
                    objetos+=1
                if r != 0 and t == 0:
                    img.itemset((i, j), r)
                if r == 0 and t != 0:
                    img.itemset((i, j), t)
                if r != 0 and t != 0 and t == r:
                    img.itemset((i, j), r)
                if r != 0 and t != 0 and t != r:
                    img.itemset((i, j), r)
                    if r > t:
                        equivalentes[r] = t
                    else:
                        equivalentes[t] = r
    for e in range(255, 0, -1):
        if equivalentes[e] != 0:
            objetos -= 1
            for i in range(0, int(linhas)):
                for j in range(0, int(colunas)):
                    if img.item(i, j) == e:
                        img.itemset((i, j), equivalentes[e])

    cv2.imshow('Imagem rotulada', img)
    cv2.imwrite('imagem_rotulada.jpg', img)
    print('Foram encontrados: ', objetos, ' objetos')


rotular('../images/bolhas.png')
cv2.waitKey(0)
cv2.destroyAllWindows()
