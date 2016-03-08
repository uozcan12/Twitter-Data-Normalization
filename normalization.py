# -*- coding:utf-8 -*-

import nltk
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer

tokenizer = WordPunctTokenizer()
token = tokenizer.tokenize('@dida bi yere gitcem "büttttttüüüünnnn insanlar hür, hysyt ve haklari bkmndn e$it doğarlaaaar.aaaaaakıl ve vicdana #sahiptirler ve birbirlerine karşi kardeslik zhnyt ile hrkt €tm€lidirl€r ." die bağırcam :)) #insanhakları www.insanhaklari.com')

#token = tokenizer.tokenize("@dida bi yere gitcem. @ugur doğarlaaaar.aaaaaakıl #insanhakları www.insanhaklari.com")
print token
for i in range(len(token)) :
    if token[i].startswith("@"):
        token[i] = "@mention[@" + token[i+1] +"]"
	token[i+1]=""
    elif token[i].startswith("#"):
        token[i] = "@hashtag[#" + token[i+1] +"]"
	token[i+1]=""
    elif token[i].startswith("www"):
        token[i] = "@url[www."
	token[i+1]=""
    elif token[i].endswith("com"):
        token[i] = ".com]"
	token[i-1]=""
    elif token[i].endswith("tcem"):
	token[i]=token[i].replace("tcem","deceğim")
    elif token[i].endswith("micem"):
	token[i]=token[i].replace("micem","meyeceğim")
    elif token[i].endswith("mıcam"):
	token[i]=token[i].replace("mıcam","mayacağım")
    elif token[i].endswith("rcam"):
	token[i]=token[i].replace("rcam","racağım")
    elif token[i].startswith("bi"):
	token[i]=token[i].replace("bi","bir")
    elif token[i].startswith("die"):
	token[i]=token[i].replace("die","diye")
    
xxx=' '.join(token)
xxx=re.sub(' +',' ',xxx)
print "\n\n" 
print xxx 

	
   
    
 
