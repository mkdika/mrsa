# coding: utf-8
# In[12]:
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
import string
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer


# to save/load trained model
from sklearn.externals import joblib


# In[13]:
#def text_process(mess):
#    nopunc = [char for char in mess if char not in string.punctuation]
#    nopunc = ''.join(nopunc)
#    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

# In[14]:
#filename = 'movieSA-model.sav'

# In[15]:
#model = joblib.load(filename)
def text_process(mess):
    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

filename = 'movieSA-model.sav'
model = joblib.load(filename)

def process_sentiment(sentiment):
    mytest = pd.Series(data=[sentiment])
    mypred = model.predict(mytest)
    return mypred[0]

# In[18]:
if __name__ == '__main__':
    comments = ["Sit back and enjoy the stunts, the speed, the style.",
               "horrible movie i ever watched!!!!",
               "John Wick: Chapter 2 is a somewhat more distanced affair. But it's still an impressively dizzying symphony of carnage.",
               "Chapter 2, with Keanu Reeves at his absolute best, is the real deal in action-movie fireworks - it's pure cinema, an adrenaline rocket of image and sound that explodes on contact."]
    #mytest = pd.Series(data=comment)


    # In[19]:

    #mypred = model.predict(mytest)
    #print(mypred)
    for comment in comments:
        print(comment, '=>', process_sentiment(comment))
