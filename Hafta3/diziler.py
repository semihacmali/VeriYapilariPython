# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
dizi = [2,5,8,1]
dizi[0]
dizi[4]

for i in range(4):
    print(dizi[i])

len(dizi)    

for i in range(len(dizi)):
    print(dizi[i])
    
for eleman in dizi:
    print(eleman)    

a = int(input("değergirin"))

sayilar = []    
for i in range(7):
    deger = int(input("değergirin"))
    sayilar.append(deger)    
    
 
sayilar    
#en büyük eleman bulma
enkucuk = sayilar[0]
print(enkucuk)
for eleman in sayilar:
    if eleman > enkucuk:
        enkucuk = eleman
print(enkucuk)           

toplam = 0 
for i in sayilar:
    toplam = toplam + i
print(toplam)    
    
dizi1 = [2,9,5,12]
dizi2 = [26,78,6,90]
dizi3 = []
for i in range(len(dizi1)):
    dizi3.append(dizi1[i] + dizi2[i])
print (dizi3)    
    
matris = [
    [4,6,9],
    [1,8,3],
    [2,12,20]
    ]    
matris[2][1]    

toplam = 0 
for i in range(len(matris)):
    for j in range(len(matris[i])):
        toplam = toplam + matris[i][j] 
print(toplam)


















    
    
    
    
    
    