#!/usr/bin/python
#coding=utf-8
import re

l=[]

f=open('filtered_word.txt','rb')
filt=f.readlines()
f.close()
pattern=re.compile('|'.join(filt).replace('\n',''))
data=raw_input("Please input a string: ")
if pattern.findall(data):
    word2=pattern.match(data).group()
    for i in range(len(word2.decode('utf-8'))):
        l.append('*')
    word=pattern.sub(''.join(l),data,len(pattern.findall(data)))
    print word
else:
    print data
