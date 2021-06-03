#Trabalho 0 do curso de Processamento de Imagem Digital
#Prof. Hélio
#Aluno: Mário Antônio Costa Júnior
#RA: 226496

#Carrega bibliotecas
import os, math, sys
from skimage import io
from skimage.viewer import ImageViewer
from skimage import util
from skimage.transform import rotate
from numpy import fliplr, flipud
import numpy as np
from PIL import Image, ImageEnhance
import pandas as pd
import cv2
from scipy.misc import imsave

#########   Exercicio 1
########################################################################################################################################################
# diretório da imagem
#filename = "C:\\Users\\PM\\Documents\\Mario\\pessoal\\Processamento Imagen Digital\\trabalho0\\Imagens\\city.png"

aux = 0
# Pega os parametros do diretorio
diret = input('Insira o caminho do diretório (ex: /home/teste/):')

File = input('Insira o nome da imagem 1 (ex: city.png):')
File1 = input('Insira o nome da imagem 2 (ex: baboo.png):')
File2 = input('Insira o nome da imagem 3 (ex: butterfly.png):')

#Verifica a existencia do caminho do diretório e os arquivos selecionados
if not os.path.exists(diret+File) and not os.path.exists(diret+File1) and not os.path.exists(diret+File2):
    print('')
    sys.exit

filename = diret+File

#Carrega a imagem a ser tratada
image = io.imread(filename)
image_copy = image

############## 1.1 ###################
# Negativo de imagem  (Atividade - B)
image = 255 - image
cv2.imshow('1.1 Atividade - B',image) 
cv2.imwrite(diret+"1.1Atividade-B.png", image) 

# Espelhamento vertical  (Atividade - C)
image = image_copy
image = fliplr(image)
image = rotate(image, angle=180)
imsave(diret+"1.1Atividade-C.png", image)
cv2.imshow('1.1 Atividade - C',image) 


# Conversão do intervalo de intensidade para  (100,200) (Atividade - D)
image = image_copy
image[image < 100] = 0
image[image > 200] = 255
cv2.imshow('1.1 Atividade - D',image) 
cv2.imwrite(diret+"1.1Atividade-D.png",image) 

# Inverte as linhas pares das imagens (iniciando pelo 0) (Atividade - E)
image = image_copy
image[0::2, :] = image[0::2, ::-1]
cv2.imshow('1.1 Atividade - E',image) 
cv2.imwrite(diret+"1.1Atividade-E.png",image) 


# Reflexão de linhas (Atividade - F)
image = io.imread(filename)
dim = image.shape
mid = math.trunc((dim[0]/2)) # carrega metade da imagem
a = image[0:mid:1]
b = image[mid::-1]
image = np.vstack((a,b))  # agrupa as imagens
cv2.imshow('1.1 Atividade - F',image) 
cv2.imwrite(diret+"1.1Atividade-F.png",image)

############## 1.2 ###################
# ajuste de brilho com imagem do baboon
# diretório da imagem
#filename = "C:\\Users\\PM\\Documents\\Mario\\pessoal\\Processamento Imagen Digital\\trabalho0\\Imagens\\baboon.png"
filename = diret+File1

# Carrega a imagem a ser tratada
image = io.imread(filename)
image_copy = image

# gama em 1.5, 2.5, 3.5
fator = 1.5
image = np.power(image/float(np.max(image)),1/fator)
cv2.imshow('Brilho fator 1.5',image)
imsave(diret+"1.2Brilho fator-1.5.png", image)
#cv2.imwrite(diret+"1.2Brilho fator-1.5.png",image)

fator = 2.5
image = np.power(image/float(np.max(image)),1/fator)
cv2.imshow('Brilho fator 2.5',image)
imsave(diret+"1.2Brilho fator-2.5.png", image)
#cv2.imwrite(diret+"1.2Brilho fator-2.5.png",image)

fator = 3.5
image = np.power(image/float(np.max(image)),1/fator)
cv2.imshow('Brilho fator 3.5',image)
imsave(diret+"1.2Brilho fator-3.5.png", image)
#cv2.imwrite(diret+"1.2Brilho fator-3.5.png",image)


############## 1.3 ###################
image = image_copy
# Pega o número de linhas e colunas
row, col = image.shape
# cria os arrays no tamanho da imagem
arr = np.zeros((row,col,8),dtype=np.uint8)
row = np.zeros((row,col,8),dtype=np.uint8)

# Plano de Bit 1
arr[:,:,1] = 2**1
row[:,:,1] = cv2.bitwise_and(image,arr[:,:,1])
mask=row[:,:,1]>0
row[mask]=255
cv2.imshow('1.3 - Plano de Bit 1',row[:,:,1])
cv2.imwrite(diret+"1.3Plano de Bit 1.png",row[:,:,1])

# Plano de Bit 4
arr[:,:,4] = 2**4
row[:,:,4] = cv2.bitwise_and(image,arr[:,:,4])
mask=row[:,:,4]>0
row[mask]=255
cv2.imshow('1.3 - Plano de Bit 4',row[:,:,4])
cv2.imwrite(diret+"1.3Plano de Bit 4.png",row[:,:,4])

# Plano de Bit 7
arr[:,:,7] = 2**7
row[:,:,7] = cv2.bitwise_and(image,arr[:,:,7])
mask=row[:,:,7]>0
row[mask]=255
cv2.imshow('1.3 - Plano de Bit 7',row[:,:,7])
cv2.imwrite(diret+"1.3Plano de Bit 7.png",row[:,:,7])


############## 1.4 ###################
# Mosaico
image = image_copy
size = np.arange(16,dtype=object).reshape((4,4))

nRows = 4  #Número de Linhas
mCols = 4  #Numero de Colunas

# Dimensions of the image
sizeX = image.shape[1]
sizeY = image.shape[0]

aux = []

for i in range(0,nRows):
    for j in range(0, mCols):
        roi = image[i*int(sizeY/nRows):i*int(sizeY/nRows) + int(sizeY/nRows) ,j*int(sizeX/mCols):j*int(sizeX/mCols) + int(sizeX/mCols)]
        size[i][j] = np.asarray(roi)
        
# concatenado original
lin1 = np.concatenate((size[0][0],size[0][1],size[0][2],size[0][3]),axis=1)
lin2 = np.concatenate((size[1][0],size[1][1],size[1][2],size[1][3]),axis=1)
lin3 = np.concatenate((size[2][0],size[2][1],size[2][2],size[2][3]),axis=1)
lin4 = np.concatenate((size[3][0],size[3][1],size[3][2],size[3][3]),axis=1)
aux = np.concatenate((lin1,lin2,lin3,lin4),axis=0)

cv2.imshow('1.4 - Mosaico (Original)', aux)
cv2.imwrite(diret+"1.4Mosaico (Original).png",aux)

# concatenado de arcordo com exercicio
lin1 = np.concatenate((size[1][1], size[2][2], size[3][0], size[0][2]),axis=1)
lin2 = np.concatenate((size[1][3], size[3][3], size[0][0], size[2][0]),axis=1)
lin3 = np.concatenate((size[2][3], size[3][1], size[0][1], size[1][2]),axis=1)
lin4 = np.concatenate((size[0][3], size[3][2], size[2][1], size[1][0]),axis=1)
aux = np.concatenate((lin1,lin2,lin3,lin4),axis=0)

cv2.imshow('1.4 - Mosaico (Nova ordem)', aux)
cv2.imwrite(diret+"1.4Mosaico (Nova ordem).png",aux)

############## 1.5 ###################
# Combinacao de imagens
#carregas as imagens

#filename2 = "C:\\Users\\PM\\Documents\\Mario\\pessoal\\Processamento Imagen Digital\\trabalho0\\Imagens\\butterfly.png"
filename2 = diret+File2
im1 = cv2.imread(filename)
im2 = cv2.imread(filename2)
# 0.2 + 0.8
sobre = cv2.addWeighted(im1,0.2,im2,0.8,0)
cv2.imshow('1.5 - Combinação de Imagem (0.2 + 0.8)', sobre)
cv2.imwrite(diret+"1.5Combinação de Imagem(0.2 + 0.8).png",sobre)
# 0.5 + 0.5
sobre = cv2.addWeighted(im1,0.5,im2,0.5,0)
cv2.imshow('1.5 - Combinação de Imagem (0.5 + 0.5)', sobre)
cv2.imwrite(diret+"1.5Combinação de Imagem(0.5 + 0.5).png",sobre)
# 0.8 + 0.2
sobre = cv2.addWeighted(im1,0.8,im2,0.2,0)
cv2.imshow('1.5 - Combinação de Imagem (0.8 + 0.2)', sobre)
cv2.imwrite(diret+"1.5Combinação de Imagem(0.8 + 0.2).png",sobre)
        
cv2.waitKey(0)