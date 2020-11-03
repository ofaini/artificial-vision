# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:48:33 2020

@author: oscar
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('images/bananas.jpg')
#cv2.imshow('New image', img1)

pxX = np.size(img1, axis=0)
pxY = np.size(img1, axis=1)

promManual = np.sum(img1) / (pxX * pxY * 3)

suma = np.sum(img1)
minimo = np.min(img1)
maximo = np.max(img1)
prom = np.mean(img1)
var = np.var(img1)#varianza
de = np.sqrt(var)#desviacion estandar

#Operaciones avanzadas

cv2.imshow("img-Original",img1)

hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
#cv2.imshow('img-HSV', hsv)

I = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#cv2.imshow('img-Gray', I)

umbral,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)
binaria = np.uint8((I<umbral)+255)
#cv2.imshow('img-Binary', binaria)

#Histograma
data = I.flatten()
plt.hist(data, bins = 100)


cv2.waitKey(0)
cv2.destroyAllWindows()