# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:40:08 2020

@author: oscar
"""

#Developer: Oscar Faini
'''
Glossary:
    imread: image read
    cv2: opencv
    Add: add images
    imshow: show images
    
    
Script description:
    1. Download 2 different images.
    2. Apply basic math operation.
        ->Add two images.
        ->Subst two images.
'''
#Import library
import cv2

def add_images(x,y):
    #the images are added
    new_image = cv2.add(x,y)
    cv2.imshow('New image',new_image)
    

#Main:::::::::::::::::::::::::::::::::
img_1 = cv2.imread('images/perro1.jpg')
img_2 = cv2.imread('images/perro1.jpg')

add_images(img_1, img_2)

cv2.waitKey(0)
cv2.destroyAllWindows()