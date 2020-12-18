# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 11:02:39 2020
Proyect 1: Exam Grader
@author: oscar
"""
'''
Glosary:
    dilate => 
    drawContours =>
    RETR_TREE => 
    thickness =>
    CHAIN_APPROX_SIMPLE =>
    (...,-1,...) =>
'''


#Libraries OpenCV, Numpy
import cv2
import numpy as np


def getAnswers(imaExam):
    #1. Canny
    can = cv2.Canny(imaExam,20,150)
    kernel = np.ones((5,5),np.uint8)
    bordes = cv2.dilate(can, kernel)
    
    #Obtener contornos
    contour,_ = cv2.findContours(
        bordes, 
        cv2.RETR_TREE, 
        cv2.CHAIN_APPROX_SIMPLE) #Sacar los contornos
    
    #Dibujar contornos
    objects = bordes.copy()
    cv2.drawContours(
        objects,
        [max(contour, key=cv2.contourArea)],-1,255,thickness=-1)
    
    #Get labels
    output = cv2.connectedComponentsWithStats(objects,4,cv2.CV_32S)
    cantObj = output[0] # Objects quantity
    labels = output[1] # Labels
    stats = output[2] #stats
    
    #Get ArgMax
    mask = np.uint8(255*(np.argmax(stats[:,4][1:])+1==labels))
    
    contours,_ = cv2.findContours(
        mask, 
        cv2.RETR_TREE, 
        cv2.CHAIN_APPROX_SIMPLE) #Sacar los contornos
    cnt = contours[0] # Puntos específicos
    
    #ConvexHull => Polígono convexo
    hull = cv2.convexHull(cnt) # Obtener puntos del polígono que se está creando
    puntoConvex = hull[:,0,:] # Generar el punto convexo
    m,n = mask.shape # Genero Dimensiones de la imagen
    ar = np.zeros((m,n)) #Crear matriz de ceros
    mascara_convex = np.uint8(
        cv2.fillConvexPoly(ar,puntoConvex,1)) # 1: Grosor de línea
    
    vertices = cv2.goodFeaturesToTrack(mascara_convex,4,0.01,20)
    
    x = vertices[:,0,0]
    y = vertices[:,0,1]
    
    vertices = vertices[:,0,:]
    
    Xx = np.sort(x)
    Yy = np.sort(y)
    
    xn = np.zeros((1,4))
    yn = np.zeros((1,4))
    
    xn = (x==Xx[2])*n+(x==Xx[3])*n
    yn = (y==Yy[2])*m+(y==Yy[3])*m
    
    verticesN = np.zeros((4,2))
    
    verticesN[:,0] = xn
    verticesN[:,1] = yn
    
    vertices = np.uint64(vertices)
    verticesN = np.uint64(verticesN)
    
    h,_ = cv2.findHomography(vertices, verticesN)
    img_2 = cv2.warpPerspective(imaExam,h,(n,m))
    r = img_2[:,np.uint64(0.25*n):np.uint64(0.84*n)]
    
    options = ['A','B','C','D','E','x']
    answers = []
    
    for i in range(0,26):
        pregunta=r[np.uint64(i*(m/26)):np.uint64((i+1)*(m/26)),:]
        sumI=[]
        for j in range(0,5):
            _,col=pregunta.shape
            sumI.append(np.sum(pregunta[:,np.uint64(j*(col/5)):np.uint64((j+1)*(col/5))])) 
        vmin=np.ones((1,5))*np.min(sumI)
        
        if np.linalg.norm(sumI-vmin)>0.17*col*m:
            sumI.append(float('inf'))
        else:
            sumI.append(-1)
        
        answers.append(options[np.argmin(sumI)])
    return answers
        
        
    #cv2.imshow('Exam - Source',imaExam)

#Main
#0. Load images
#imaExam = cv2.imread('images/Cal_1.jpg',0)
imaExam = cv2.imread('images/Cal_2.jpg',0)
#imaExam = cv2.imread('images/Cal_3.jpg',0)
respuestasFormato = np.array(getAnswers(imaExam))
respuestasCorrectas = np.array(['B','C','D','E','B','C','C','A','A','B','C','A','E','A','A','B','C','A','A','B','C','A','A','B','C','A'])

calFinal= 5*np.sum(respuestasCorrectas==respuestasFormato)/26

cv2.waitKey(0)
cv2.destroyAllWindows()