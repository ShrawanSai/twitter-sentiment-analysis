import os
import pickle
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

def predict():
   path_test_data=os.getcwd()+'/livestream1.txt'
   import cleaner

   print('Importing the trained classifier ')
   f = open('da_classifier.pickle', 'rb')
   clss = pickle.load(f)
   f.close()
   ###### get vectorizer ######
   f = open('da_vectorizer.pickle', 'rb')
   vectorizer = pickle.load(f)
   f.close()

   #load the data

   data=[]

   eval_data=open(path_test_data,'r')

   for sent_msg in eval_data:
      data.append(' '.join(sent_msg.split())) #copied from sample code in github
   df= pd.DataFrame(data)
   #print(data)
   df=df[0]
   #print(df)
   #cleaning the data and parsing

   clean_data=[]

   for i in df:
      clean_data.append(i)
   xxxxx=clean_data
   clean_data=cleaner.clean(clean_data)
   count_vectorized_data=vectorizer.transform(clean_data)

   np.asarray(count_vectorized_data)

   tfidf_trans=TfidfTransformer()

   X_data_tfidfed=tfidf_trans.fit_transform(count_vectorized_data)

   ####
   predictions=clss.predict(X_data_tfidfed)

   conf=clss.predict_proba(X_data_tfidfed)
   #print(conf)

   final=pd.DataFrame(data={'Tweet':xxxxx,'Sentiment':predictions})

   print('making predictions')
   pred_result=list(predictions)
   #print(predictions)

   print('Creating files : Bag of words and the final submission')
   final.to_csv(('New_bag_of_words.csv'), index=False, quoting=3, escapechar='\\',sep='~')
   final.to_csv(('output.txt'), index=False, quoting=3, escapechar='\\',sep='~')
   print('Done. Check folder')
   return (xxxxx,predictions)
