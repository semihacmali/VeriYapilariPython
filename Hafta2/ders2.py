# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def EkranaYazma():
    print("iclal")
    
#EkranaYazma=5
#print(EkranaYazma)

EkranaYazma()

def IcerdenDisari():
    sayi=6
    return sayi
  
sayi2=7 
sayi3=3    
print(str(sayi2+sayi3))
print(str(sayi2+IcerdenDisari()))

def Toplama(sayi1,sayi2):
    toplam=sayi1+sayi2
    print(str(toplam))

Toplama(5,7)

#taban=2 ust=3 2*2*2
def UstAlma(taban,ust):
    sonuc=1
    for i in range(ust):
        sonuc=sonuc*taban
    return sonuc
        
UstAlma(2, 3)

UstAlma(ust=3, taban=2)

def REUstAlma (taban, ust):
    if ust==0:
        return 1
    elif ust==1:
        return taban
    else :
     return taban * REUstAlma(taban, ust-1)




REUstAlma(taban=2, ust=1000)

def faktorteriyel(n):
    sonuc= 1
    for i in range (1 , n + 1):
        return sonuc 
print ("7!" + faktorteriyel(7))

def REFaktoriyel(sayi):
    if sayi == 0 or sayi == 1:
        return 1
    else:
        return sayi * REFaktoriyel(sayi - 1)
    
REFaktoriyel(0)


    







