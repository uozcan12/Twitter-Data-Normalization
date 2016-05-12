'''
Created on Mar 10, 2016

@author: ugur
'''


metin=input("Lütfen bir metin giriniz: ")
harf=[]
sayi=[]
for i in(metin):
    if not (i in harf):
        harf.append(i)
        sayi.append(1)
    else:
        sayi[harf.index(i)]=sayi[harf.index(i)]+1
print ("Harf --> Sayi")
for j in range(len(harf)):
    print (harf[j], " --> ", sayi[j])
    