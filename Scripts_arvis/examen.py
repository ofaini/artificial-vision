# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:46:13 2020

@author: oscar
"""

list = ["1,2,3,4","7,8,9,10,5"]

listA = list[0].split(sep=',')
listB = list[1].split(sep=',')

i=0
counter=0
while i< len(listA):
    j=0
    while j < len(listB):
        j=0
        while j < len(listB):
            if listA[i] == listB[j]:
                print ("lista",listA[i])
                counter+=1
            j+=1
        i+=1
    if counter == 0:
        print("None")