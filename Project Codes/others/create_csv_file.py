# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:37:10 2020

@author: Karate Kid
""
# -*- coding: utf-8 -*-
"""

import pandas as pd
import csv



tokenized_word=[]
raw_data = pd.read_csv('dataset_labelled.csv')
#print(raw_data)    

clas = raw_data["class"]
tweet = raw_data["tweet"]

hate=[]
offensive=[]
neutral=[]

for i in range(len(clas)):
    if clas[i] == 0:
        hate.append(tweet[i])
        
    elif clas[i] == 1:
        offensive.append(tweet[i])
        
    else:
        neutral.append(tweet[i])

df = pd.DataFrame(hate, columns=["tweet"])
df.to_csv('hate.csv', index=False)

df = pd.DataFrame(offensive, columns=["tweet"])
df.to_csv('offensive.csv', index=False)

df = pd.DataFrame(neutral, columns=["tweet"])
df.to_csv('neutral.csv', index=False)

