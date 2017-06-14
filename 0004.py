import re

count=0

f=open('words.txt','rb')
pattern=re.compile(r'[a-zA-Z]+')
for data in f.readlines():
    count+=len(pattern.findall(data))
f.close()

print count
