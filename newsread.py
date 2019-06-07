import bs4 as bs
import urllib.request
import nltk
from nltk.tree import Tree
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.corpus import treebank_chunk,state_union
source = urllib.request.urlopen('https://www.rediff.com/news/headlines').read()
soup = bs.BeautifulSoup(source,'lxml')
#print(soup)


####

def get_continuous_chunks(text):
     chunked = ne_chunk(pos_tag(word_tokenize(text)))
     continuous_chunk = []
     current_chunk = []
     for i in chunked:
             if type(i) == Tree:
                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
             elif current_chunk:
                     named_entity = " ".join(current_chunk)
                     if named_entity not in continuous_chunk:
                             continuous_chunk.append(named_entity)
                             current_chunk = []
             else:
                     continue
     return continuous_chunk
c=0
listnews=[]

for url in soup.find_all('a'):
    if 'india news' in url.text.lower():
        c=1
        continue
    if c==1:
        #print(url.text)
        
        if 'headlines' in url.text.lower():
            c=0
            break
        listnews.append(url.text)
#print(listnews)
news=[]
for i in range(len(listnews)):
    if len(listnews[i])!=0:
        news.append(listnews[i])
#print(news)

keywords=[]
def process_content():
    try:
            for i in news:
                x=get_continuous_chunks(i)
                keywords.append(x)
                #print(x)
    except Exception as e:
        print(str(e))
        
    
        

process_content()
#print(keywords)

cleanedkeywords=[]
for i in range(len(keywords)):
    if len(keywords[i])!=0:
        cleanedkeywords.append(keywords[i])
        
ckw=cleanedkeywords

kw=[]
for i in range(len(ckw)):
    for j in range(len(ckw[i])):
        kw.append(ckw[i][j])
print(kw)


def returncleaned():
    return kw
        
