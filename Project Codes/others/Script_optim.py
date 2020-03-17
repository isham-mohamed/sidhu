# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:16:06 2020

@author: Karate Kid
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:34:58 2020

"""
import nltk
import csv
import numpy 
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
import pickle
import simplejson 
import pandas as pd
import string 
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def write_file(filename,word):
    with open(filename,'w') as f:
        for item in word:
            #f.write("%s\n" % item)
            f.write(item)
    f.close()
    
def write_file_list(filename,word_list):
    f = open(filename,'w')
    simplejson.dump(word_list, f)
    f.close()    
    
    
    
 #opening csv file and storing data into variable data   
raw_data = pd.read_csv('dataset_labelled.csv')
tokenized_word=[]
data1 = raw_data['tweet']            #only taking data from column tweet

 
string1 = ' '.join(map(str, data1))   #conversion of list/series type to string


lower_data = string1.lower()

no_remove = re.sub(r'\d+', '', lower_data)
#write_file("no_remove.txt",no_remove)

     
pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
url_remove = pattern.sub('', no_remove)


special_remove = (url_remove.translate({ord(i): None for i in '#$%@!^&*()'}))
#write_file("umh_remove.txt",special_remove)


translator = str.maketrans('', '', string.punctuation)
punct_remove = no_remove.translate(translator)
#write_file("punct_remove.txt",punct_remove)



with open('punct_remove.txt','r') as f5:
    for line in f5:
        for word in line.split():   #tokeninzing while reading from txt file
            tokenized_word.append(word) #appending each word into list
f5.close()


prefixes = ('http')
for word in tokenized_word[:]:
    #if word.startswith(prefixes):
    if prefixes in word:
        tokenized_word.remove(word)
#write_file_list("token_data.txt",tokenized_word)


#unpickling code
'''with open ('outfile', 'rb') as fp:
    itemlist = pickle.load(fp)'''



stop_words = set(stopwords.words('english')) 
filtered_sentence = [] 
  
for w in tokenized_word: 
    if w not in stop_words: 
        filtered_sentence.append(w)

lemmatizer=WordNetLemmatizer()
lemm_words = []
for word in filtered_sentence:
    lemm_words.append(lemmatizer.lemmatize(word))

#write_file_list("lemmatized_words.txt",lemm_words)


















    