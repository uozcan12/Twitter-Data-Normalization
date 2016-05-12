'''
Created on Apr 10, 2016

@author: ugur
'''
import collections
import difflib
from orca.speech_generator import UPPERCASE


text_file = open("/home/ugur/Dersler/Natural Processing Language/turkce_sozluk2.txt", "r")
asli=text_file.readlines()
print(len(asli))
print("****")
[asli.remove(item) for item, count in collections.Counter(asli).items() if count > 1]
print(len(asli))
print("****")


for i in asli:
    if i==" ":
        asli.remove(i)
           
    if i.isupper() :
        i.lower()
    
            
print(len(asli))
for i in range(len(asli)):
    if asli[i].endswith("\n"):
        asli[i]=asli[i].replace("\n","")
      

print("\n")

word = input("Kelime girin : ")
ugur5=difflib.get_close_matches(word, asli)
print(ugur5)

 

  


'''     
ugur3=["ali","veli","deli"," "," "," ","ALİİ"]
print(len(ugur3))

for i in range(len(ugur3)):
    if ugur3[i]==" ":
        ugur3.remove(ugur3[i])
           
    if ugur3[i].isupper() :
        print (ugur3[i])
        
print(len(ugur3))  ''' 

        
        