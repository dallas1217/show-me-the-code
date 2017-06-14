#!/usr/bin/python
#coding=utf-8
import re

f=open('filtered_words.txt','rb')
filt=f.readlines()
f.close()
pattern='|'.join(filt).replace('\n','')
data=raw_input("Please input a string: ")
if re.findall(pattern,data):
    print "Freedom"
else:
    print "Human Rights
