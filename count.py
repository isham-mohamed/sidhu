
import json as simplejson
from collections import Counter
import os
os.chdir('/Users/ishammohamed/PycharmProjects/sidhu/Project Codes/offensive_ngram/bigrams')
print("os set")
file_list = os.listdir('/Users/ishammohamed/PycharmProjects/sidhu/Project Codes/offensive_ngram/bigrams')
#print(file_list)
#file_list.sort()
lineList = []
dup={}
dup_fname={}
c=len(file_list)
c0=1#file no.
for filename in file_list:
    f = open(filename,'r')
    print(c0,"/",c,"===",filename)
    c0+=1
    flag=0
    flag_for_line={}
    for line_text in f:
      line_text=line_text.rstrip()
      #print(line_text)
      lineList.append(line_text)
      if line_text in dup.keys():
        dup[line_text]+=1
      else:
        dup[line_text]=1
      if line_text not in flag_for_line:
          flag_for_line[line_text]=0
      if flag_for_line[line_text]==0:
          flag_for_line[line_text]+=1
          if line_text in dup_fname.keys():
            dup_fname[line_text]+=1
          else:
            dup_fname[line_text]=1
    f.close()
#print(lineList)
'''
print("!!!!...................word count...........!!!!")
for key in dup.keys():
  if dup[key]>1:
    print(key,"=",dup[key])
print("!!!!...................file count............!!!!")
for key in dup_fname.keys():
  if dup_fname[key]>1:
    print(key,"=",dup_fname[key])
'''

print("!!!!..........Program ended..........!!!!")

"""
l=[]
for item in dup.keys():
  l.append([item,dup[item],dup_fname[item]])
"""
import csv
# field names
fields = ['Bigram', 'word count', 'file count']

# name of csv file
filename = "table.csv"

# writing to csv file
with open('/Users/ishammohamed/PycharmProjects/sidhu//Project Codes/offensive_ngram/output/'+filename, 'w') as csvfile:
  # creating a csv writer object
  csvwriter = csv.writer(csvfile)
  # writing the fields
  csvwriter.writerow(fields)
  # writing the data rows
  for item in dup.keys():
    csvwriter.writerow([item,dup[item],dup_fname[item]])