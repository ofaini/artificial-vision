# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:52:01 2020

@author: oscar
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('images/A.jpg')
img2 = cv2.imread('images/B.jpg')

#visualizar imagenes en Escala de Grises
I = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
H = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#umbral de las dos imagenes
umbralA,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)
umbralB,_ = cv2.threshold(H,0,255,cv2.THRESH_OTSU)
#imagenes Binarias
mascaraA = np.uint8((I<umbralA)+255)
mascaraB = np.uint8((H<umbralB)+255)


sumaA = np.sum(img1)
sumaB = np.sum(img2)
minimoA = np.min(img1)
minimoB = np.min(img2)
maximoA = np.max(img1)
maximoB = np.max(img2)
promA = np.mean(img1)
promB = np.mean(img2)
varA = np.var(img1)
varB = np.var(img2)
desA = np.sqrt(varA)
desB = np.sqrt(varB)

#Get labels
outputA = cv2.connectedComponentsWithStats(mascaraA,0,cv2.CV_32F)
cantObjA = outputA[0] # Objects quantity
outputB = cv2.connectedComponentsWithStats(mascaraB,0,cv2.CV_32F)
cantObjB = outputB[0] # Objects quantity

#Histograma
dataA = I.flatten()
plt.hist(dataA, bins = 100)
dataB = H.flatten()
plt.hist(dataB, bins = 100)

#Suma de imagenes
resSum = cv2.add(img1,img2)

#imshow
cv2.imshow("Suma imagenes",resSum)

cv2.waitKey(0)
cv2.destroyAllWindows()