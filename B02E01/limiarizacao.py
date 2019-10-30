import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def histograma(imagem):
    plt.hist(imagem.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()

def limiarizar(imagem, limiar):
    imagemBin = cv2.threshold(imagem, limiar, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("Imagem limiarizada", imagemBin)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def limiarizarOpenCv(imagem):
    imagemBin = cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 1)
    cv2.imshow("Imagem limiarizada", imagemBin)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def limiarAdaptativoGlobal(imagem, deltat):
    anterior = 255
    atual = 127
    totalG1=0
    qtdG1=0
    totalG2=0
    qtdG2=0
    while(abs(anterior-atual)>deltat):
        linhas, colunas = imagem.shape
        for i in range(0, linhas):
            for j in range(0, colunas):
                if(imagem.item(i, j)<=atual):
                    totalG1=totalG1+imagem.item(i, j)
                    qtdG1+=1
                else:
                    totalG2=totalG2+imagem.item(i, j)
                    qtdG2+=1
        anterior=atual
        atual=int(((totalG1/qtdG1)+(totalG2/qtdG2))/2)
    limiarizar(imagem, atual)


def menu():
    cls()
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Histograma")
    print ("2. Aplicar limiar manualmente")
    print ("3. Limiar Global adaptativo")
    print ("4. Limiar adaptativo Opencv")
    print ("5. Sair")
    print (67 * "-")

img = cv2.imread('../images/dog2.jpg', cv2.IMREAD_GRAYSCALE)
tecla=0
loop=True      
  
while loop:
    menu()
    escolha = input("Escolha uma opcao [1-5]: ")
    if escolha=='1':     
        histograma(img)
    elif escolha=='2':
        limiar = int(input("Entre com um limiar: "))
        limiarizar(img, limiar)
    elif escolha=='3':
        limiarAdaptativoGlobal(img, 0)
    elif escolha=='4':
        limiarizarOpenCv(img)
    elif escolha=='5':
        loop=False
    else:
        print("Entrada incorreta, tente novamente..")


cv2.destroyAllWindows()