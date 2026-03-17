# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script 
"""
sayilar = [ 9,8,5,4,2]

for i in range(len(sayilar)):
    #print(sayilar[i])
    enkucuk = sayilar[i]
    indis = i
    for j in range(i+1,len(sayilar)):
        #print(sayilar[j])
        if enkucuk > sayilar[j]:
            enkucuk = sayilar[j]
            indis = j
    sayilar[i],sayilar[indis] = sayilar[indis],sayilar[i]        
    print(sayilar)

def SelectionSort(sayilar):
    for i in range(len(sayilar)):
        #print(sayilar[i])
        enkucuk = sayilar[i]
        indis = i
        for j in range(i+1,len(sayilar)):
            #print(sayilar[j])
            if enkucuk > sayilar[j]:
                enkucuk = sayilar[j]
                indis = j
        sayilar[i],sayilar[indis] = sayilar[indis],sayilar[i]
    return sayilar                   
a = [8,6,4,23,15,74,5,-3]

b = SelectionSort(a)


sayilar = [9,7,6,5,3,2,1]
for i in range(len(sayilar), 0, -1):
    #print(i)
    for j in range(0, i-1):
        #print(j)
        if sayilar[j]> sayilar[j+1]:
            sayilar[j],sayilar[j+1]= sayilar[j+1],sayilar[j]
    print(sayilar)

def BubbleSort(sayilar):
    for i in range(len(sayilar), 0, -1):
        #print(i)
        for j in range(0, i-1):
            #print(j)
            if sayilar[j]> sayilar[j+1]:
                sayilar[j],sayilar[j+1]= sayilar[j+1],sayilar[j]
    return sayilar

x = [6,0,-5,86,9,1,3,4]
y = BubbleSort(x)
y

















