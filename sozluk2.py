import collections
import difflib
from _ast import alias


def unforgotten(word):

    text_file = open("/home/ugur/Dersler/Natural Processing Language/turkce_sozluk2.txt", "r")
    asli=text_file.readlines()
    text_file.close()
   # print(len(asli))
    print("****")
    ugur1="".join(asli)

    ugur1=ugur1.replace(" ","\n")
    ugur1=ugur1.replace(" ","\t")
    ugur1=ugur1.lower()

    ugur2=ugur1.split("\n")

    ugur3=[]        
    [ugur3.append(item) for item, count in collections.Counter(ugur2).items() if count >=1 ]        
    ugur4=[]

    for x in sorted(ugur3):
        ugur4.append(x)
   

    text_file2 = open("/home/ugur/Dersler/Natural Processing Language/turkce_sozluk2.txt", "w")
    for item in ugur4:
        text_file2.write("%s\n" % item)

    text_file.close()    

    ugur5=difflib.get_close_matches(word, ugur4)
    return ugur5
    

a=["hysyt","bkmndn","hrkt","zhnyt","cnm","yazsm","nslsn","glyn","npysn"]

for i in range(len(a)) :
    print(unforgotten(a[i]))



  


        