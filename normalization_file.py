# -*- coding:utf-8 -*-

import nltk
import re
import difflib
from deasciifier import Deasciifier
from nltk.tokenize import word_tokenize
import collections
from nltk.tokenize import WordPunctTokenizer


text_file = open("/home/ugur/Desktop/aslihan_nlp/mydata2.txt", "r")
asli=text_file.readlines()

before_normalize=' '.join(asli)
before_normalize=re.sub(' +',' ',before_normalize)
#print (before_normalize)

print ("##################################################")

tweet_nltk=before_normalize.split(" ")

########### STEP  : SPEACIAL SIGNS

print (tweet_nltk)
for i in range(len(tweet_nltk)) :
    if "$" in tweet_nltk[i]:
        tweet_nltk[i]=tweet_nltk[i].replace("$","ş")
       
    elif "£" in tweet_nltk[i]:
        tweet_nltk[i]=tweet_nltk[i].replace("£","e")
        
    elif "€" in tweet_nltk[i]:
        tweet_nltk[i]=tweet_nltk[i].replace("€","e")
          
tweet2=' '.join(tweet_nltk)
tweet2=re.sub(' +',' ',tweet2) 
print ("\n\n")  
#print (tweet + "\n\n")  

ugur=[]

########### STEP  : EMPHASIZE WORDS

class groupby:
    # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
    # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
    def __init__(self, iterable, key=None):
        if key is None:
            key = lambda x: x
        self.keyfunc = key
        self.it = iter(iterable)
        self.tgtkey = self.currkey = self.currvalue = object()
    def __iter__(self):
        return self
    def __next__(self):
        while self.currkey == self.tgtkey:
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)
        self.tgtkey = self.currkey
        return (self.currkey, self._grouper(self.tgtkey))
    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            try:
                self.currvalue = next(self.it)
            except StopIteration:
                return
            self.currkey = self.keyfunc(self.currvalue)

for k, g in groupby(tweet2):
    ugur.append(k) 

tweet3="".join(ugur)

   
tokenizer = WordPunctTokenizer()
token = tokenizer.tokenize(tweet3)

print (token)

for i in range(len(token)) :
    if token[i].startswith("@"):
        token[i] = "@mention[@" + token[i+1] +"]"
        token[i+1]=""
    elif token[i].startswith("#"):
        token[i] = "@hashtag[#" + token[i+1] +"]"
        token[i+1]=""
    elif token[i].startswith("w"):
        if token[i+1].startswith("."):
            token[i] = "@url[www" + token[i+1]
            token[i+1]=""
    elif token[i].startswith("ht p"):
        if token[i+1].startswith("."):
            token[i] = "@url[http" + token[i+1]
            token[i+1]=""        
    elif token[i].endswith("com"):
        token[i] = token[i-1]+"com]"
        token[i-1]=""
    elif token[i].endswith("tcem"):
        token[i]=token[i].replace("tcem","deceğim")
    elif token[i].endswith("tçem"):
        token[i]=token[i].replace("tçem","deceğim")    
    elif token[i].endswith("micem"):
        token[i]=token[i].replace("micem","meyeceğim")
    elif token[i].endswith("mıcam"):
        token[i]=token[i].replace("mıcam","mayacağım")
    elif token[i].endswith("rcam"):
        token[i]=token[i].replace("rcam","racağım")
    elif token[i].endswith("pcam"):
        token[i]=token[i].replace("pcam","pacağım")    
    elif token[i].startswith("bi"):
        if token[i].startswith("bir"):
            continue
        else :  
            token[i]=token[i].replace("bi","bir")
    elif token[i].startswith("die"):
        token[i]=token[i].replace("die","diye")

########### STEP  : FORGOTTEN LETTERS IN WORDS

def unforgotten(word):

    text_file = open("/home/ugur/Dersler/Natural Processing Language/turkce_sozluk2.txt", "r")
    asli=text_file.readlines()
    text_file.close()
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

    ugur5=difflib.get_close_matches(word, ugur4)[0]
    return ugur5

for i in range(len(token)):
    if token[i].find("a")==-1 :
        if token[i].find("e")==-1 :
            if token[i].find("ı")==-1 :
                if token[i].find("i")==-1 :
                    if token[i].find("o")==-1 :
                        if token[i].find("ö")==-1 :
                            if token[i].find("u")==-1 :
                                if token[i].find("ü")==-1 :
                                    if (token[i].find(" ")!=-1 or token[i].find('"')!=-1 or 
                                        token[i].find(",")!=-1 or token[i].find(".")!=-1 or token[i].find(":)")!=-1  ) :
                                        continue
                                    elif (token[i]=="mrb" or token[i]=="merhb") :
                                        token[i]=token[i].replace(token[i],"merhaba")
                                    elif (token[i]=="aeo" or token[i]=="a.e.o" or token[i]=="a. e. o") :
                                        token[i]=token[i].replace(token[i],"allaha emanet ol")    
                                    elif (token[i]=="slm" or token[i]=="selm") :
                                        token[i]=token[i].replace(token[i],"selam")
                                    elif (token[i]=="ii" or token[i]=="i i") :
                                        token[i]=token[i].replace(token[i],"iyi")    
                                    elif (token[i]=="ii" or token[i]=="i i") :
                                        token[i]=token[i].replace(token[i],"iyi") 
                                    elif token[i]=="glyn" :
                                        token[i]=token[i].replace(token[i],"geliyorsun")
                                    elif token[i]=="ltf" or token[i]=="ltfn" :
                                        token[i]=token[i].replace(token[i],"lütfen")
                                    elif token[i]=="hrkt" :
                                        token[i]=token[i].replace(token[i],"hareket")        
                                    elif token[i]=="slcm" or token[i]=="sylcm" or token[i]=="sylcm" :
                                        token[i]=token[i].replace(token[i],"söyleyeceğim")         
                                    
                                    else : 
                                        token[i]=token[i].replace(token[i],unforgotten(token[i]))
                                        
                                         
                                else:
                                    continue      
                            else:
                                continue    
                        else:
                            continue 
                    else:
                        continue 
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue
        
    
xxx=' '.join(token)
xxx=re.sub(' +',' ',xxx)
print ("\n\n") 

########### STEP  : EMOJİ

emojis=    {'(=^..^=)' : '@gülümseyen kedi[(=^..^=)]', 
             '(=^.^=)'  : '@gülümseyen kedi[(=^.^=)]',
    '(N)'      : '@beğenmedim[(N)]',
    '(Y)'      : '@beğendim[(Y)]',
    '(]:{'     : '@sarıklı hoca[(]:{]',
    '(n)'      : '@beğenmedim[(n)]',
    '(y)'      : '@beğendim[(y)]',
    '<@%'      : '@arı[<@%]',
    '-_-'      : '@ifadesiz yüz[-_-]',
    ':"('      : '@göz yaşları dinmeyen yüz[:"(]',
    ":'("      : "@ağlayan yüz[:'(]",
    ':('       : '@üzgün surat[:(]',
    ':(:)'     : '@üzgün domuz[:(:)]',
    ':(|)'     : '@üzgün maymun[:(|)]',
    ':)'       : '@gülümseyen yüz[:)]',
    ':*'       : '@öpücük veren yüz[:*]',
    ':-('      : '@sırıtan ve içten pazarlıklı yüz[:-(]',
    ':-)'      : '@gülümseyen yüz[:-)]',
    #####################################################
    ':-*' : '@öpücük veren yüz[:-*]',
    ':-/' : '@üzgün gülümseme[:-/]',
    ':-/' : '@üzgün gülümseme[:-/]',
    ':-D' : '@kahkaha atan yüz[:-D]',
    ':-O' : '@şaşıran yüz[:-)]',   
    ':-P' : '@dil çıkaran gülümseme[:-P]',
    ':-S' : '@üzülen yüz[:S]',  
    "':-\'" : '@üzgün gülümseme', 
    ':/' : '@üzgün gülümseme[:/]',
    ':3' : '@aşık kedi[',
    ':D' : '@kahkaha atan yüz[:D]',
    ':O' : '@afallayan gülümseme[:O]',
    ':P' : '@dil çıkaran gülümseme[:P]',
    ':S' : '@üzgün gülümseme[:S]',
    ':X)' : '@gülümseyen kedi[',
    #####################################################
    '":\"' : '@üzgün gülümseme[:\]',
    ':o' : '@afallayan gülümseme[:o]',
    ':p' : '@dil çıkaran gülümseme[:p]',
    ':s' : '@üzgün gülümseme[:s]',
    ':|' : 'ifadesiz yüz[:|]',
    ';)' : 'göz kırpan yüz[;)]',
    ';*' : '@aşkla öpücük veren yüz[;*]',
    ';-)' : '@gülümseyen yüz[;-)]',
    ';-*' : '@aşkla öpücük veren yüz[;-*]',
    ';-P' : '@dil çıkaran gülümseme[;-P]',
    ';-p' : '@dil çıkaran gülümseme[;-p]',
    ';P' : '@dil çıkaran gülümseme[;P]',
    ';_;' : '@ağlayan yüz[;_;]',
    ';p' : '@dil çıkaran gülümseme[;p]',
    '</3' : '@kırık kalp[</3]',
    '<3' : '@kalp[<3]',
    '<\3' : '@kırık kalp[<\3]',
    "='(" : '@ağlayan yüz',
    '=(' :'@mutsuz yüz[=(]'  ,
    #####################################################
    '=)' : '@gülümseyen yüz[=)]',
    '=*' : '@öpücük atan yüz[*=]',
    '=/' : '@üzgün gülümseme[=/]',
    '=D' : '@kahkaha atan yüz[=D]',
    '=O' : '@afallayan gülümseme[=O]',
    '=P' : '@dil çıkaran gülümseme[=]',
    'B)' : '@hava atan gülümseme[B)]',
    'B-)' : '@hava atan gülümseme[B-)]',
    #####################################################
    'D:' : 'hayal kırıklığına uğramış yüz[D:]',
    'O.O' : '@afallayan gülümseme[O.O]',
    'O:)' : '@gülümseyen melek yüz[O:)]',
    'O:-)' : '@gülümseyen melek yüz[O:)]',
    'O=)' : '@gülümseyen melek yüz[O=)]',
    '^_^;;' : '@alnından soğuk terler döken gülümseme[^_^;;]',
    'u_u' : '@morali bozuk gülümseme[u_u]',
    #####################################################
    '}:)' : '@şeytani[}:)]',
    '}:-)' : '@şeytani[}:-)]',
    '}=)' : '@şeytani[}=)]',
    '~@~' : '@insanpisliği[~@~]'}

for emo in emojis :
    xxx=xxx.replace(emo,emojis[emo])
 

########### STEP  : DEASCIIFIER
my_ascii_turkish_txt = xxx
deasciifier = Deasciifier(my_ascii_turkish_txt)
my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
print (my_deasciified_turkish_txt)

print ("\n\n")




#my_ascii_turkish_txt = "Opusmegi cagristiran catirtilar."
#deasciifier = Deasciifier.convert_to_turkish()
#my_deasciified_turkish_txt = deasciifier.convert_to_turkish()
#print my_deasciified_turkish_txt.encode("utf-8")
 
 
    
 
