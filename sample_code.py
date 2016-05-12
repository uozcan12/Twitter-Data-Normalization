

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
ugur=[]
asli=[]           
for k, g in groupby('@dida bi yere gitcem "büttttttüüüünnnn insanlar hür, hysyt ve haklari bkmndn e$it doğarlaaaar.aaaaaakıl ve vicdana #sahiptirler ve birbirlerine karşi kardeslik zhnyt ile hrkt €tm€lidirl€r ." die bağırcam :)) #insanhakları www.insanhaklari.com'):
    ugur.append(k)
[asli.append(g) for k, g in groupby('AAAABBBCCD')]

print (asli)  
       
indigo="".join(ugur)   
print (ugur)
print (indigo)   