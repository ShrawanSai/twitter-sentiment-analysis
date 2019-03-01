import os
import pandas as pd
import numpy as np
import re
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score
import cleaner
#####

path_training_data=os.getcwd()+'/twitterdatatrain.csv'

cols = ['sentiment','id','date','query_string','user','text'] 
data=pd.read_csv(path_training_data,header=None, names=cols,encoding='latin-1')


print('_______________________________________________________')
#print(len(data))
#print(data.head())


data.drop(['id','date','query_string','user'],1,inplace=True)



X=data['text']
print(type(X))
print(X[:5])
y=data['sentiment']
clean_training_data= cleaner.clean(X)
#print('_______________________________________________________')
print(len(X))
print(y[:250])
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.02,random_state=0)

print(99999999999999999999)

vectorizer=CountVectorizer(ngram_range=(1,2))

training_features=vectorizer.fit_transform(X_train)

print(8888888888888888888888)

np.asarray(training_features)
   #now to create the tfidf thing

tfidf_vec=TfidfTransformer()
X_train_tfidfvec=tfidf_vec.fit_transform(training_features)
print(77777777777777777777777777)

classifier=svm.SVC(probability=True)
print(666666666666666666666666)


classifier.fit(X_train_tfidfvec,y_train)

print(5555555555555555)

'''

testing_features=vectorizer.fit_transform(y_train)

np.asarray(testing_features)

X_test_tfidfvec=tfidf_vec.fit_transform(testing_features)



ypredict= classifier.predict(X_test_tfidfvec)

mse= mean_squared_error(ytest,ypredict)
print(mse)'''



   #time to save classifer and vectorizer

import pickle

f=open('da_classifier.pickle','wb')
pickle.dump(classifier,f)
f.close()

g=open('da_vectorizer.pickle','wb')
pickle.dump(vectorizer,g)
g.close()

