# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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

import random
liste = [random.randint(1, 100) for _ in range(20)]

liste = SelectionSort(liste)
aranansayi = 77 
for i in range(len(liste)):
    if aranansayi >= liste[i]:
        if aranansayi == liste[i]:
            print("aranan değer listenin içinde var")
            break
    else:
        print("aranan değer listenin içinde YOK!!")
        break
    
def SiraliArama(liste, aranansayi):
    for i in range(len(liste)):
        if aranansayi >= liste[i]:
            if aranansayi == liste[i]:
                print("aranan değer listenin içinde var")
                return i
                break
        else:
            print("aranan değer listenin içinde YOK!!")
            return -1
            break    
    
def IkiliArama(liste, aranansayi):
    if len(liste) >= 1:
        if aranansayi == liste[len(liste)//2]:
            print("Aranan Degeri Bulduk!!!")
            return aranansayi
        elif aranansayi < liste[len(liste)//2]:
            return IkiliArama(liste[:len(liste)//2], aranansayi)
        elif aranansayi > liste[len(liste)//2]:
            return IkiliArama(liste[len(liste)//2:], aranansayi)    
        else:
            print("Aranan Deger Listede YOK!!!")
            return -1
    else:
        print("Aranan Deger Listede YOK!!!")
        return -1
aranansayi = 93    
IkiliArama(liste, aranansayi)    
 
import time    
ts1 = time.time()
ts2 = time.time()    
    
print(ts2-ts1)    

liste = [random.randint(1, 100000) for _ in range(100000)]    
liste = SelectionSort(liste)    
        
ts1 = time.time()
SiraliArama(liste, 99998)
ts2 = time.time()    
print("Sıralı Aramanın İşlem Süresi")    
print(ts2-ts1)  

ts1 = time.time()
IkiliArama(liste, 99998)
ts2 = time.time()    
print("İkili Aramanın İşlem Süresi")      
print(ts2-ts1)  



