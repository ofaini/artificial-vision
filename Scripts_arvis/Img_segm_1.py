# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:33:10 2020

@author: oscar
"""
import cv2
import numpy as np

img1 = cv2.imread('images/lunar_cancer.jpg')
I = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
umbral,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)#THRESH_OTSU metodo para el umbral dinamico
mascara = np.uint8((I<umbral)+255) #Binary image

#cv2.imshow("Img-COLOR",img1)
#cv2.imshow("Img-GRAY",I)
cv2.imshow("Img-BINARY",mascara)

#Get labels
output = cv2.connectedComponentsWithStats(mascara,0,cv2.CV_32F)
cantObj = output[0] # Objects quantity
labels = output[1] # Labels
stats = output[2]

#Get ArgMax
mascara = (np.argmax(stats[:,4][1:])+1==labels)

cv2.waitKey(0)
cv2.destroyAllWindows()