#from nltk.tokenize import word_tokenize
import re
####

def clean(L):
    #print(L)
    X=[]
    for i in range(len(L)):
        j = re.sub('@[a-zA-Z0-9]+',  ' ', L[i])  #removing@ symbol
        j1=re.sub('.com', ' ',j) #removing .com
        j2=re.sub('http[a-zA-Z0-9/]*',' ',j1) #removing https
        j4=re.sub('[^A-Za-z0-9-()"#@;:<>{}`+=~|.!?,]+', ' ', j2)
        j5=re.sub('u[0-9]+',' ',j4)
        j6=re.sub('RT :',' ',j5)
        j3=j6.lower()
        m=j3.split()
        j4=(" ".join(m))
        #print(j4)
        X.append(j4)
    return(X)
