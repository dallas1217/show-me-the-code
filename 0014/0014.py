#!/usr/bin/python
#coding=utf-8

from xlwt import *

def load_txt(txt):
    dic={}
    f=open(txt,'rb')
    line=f.readlines()
    dic=eval(''.join(line))
    return dic

def input_info(dic):
    w=Workbook()
    sheet=w.add_sheet('Sheet1',cell_overwrite_ok=True)
    for key in dic.keys():
        sheet.write(int(key)-1,0,key)
        for i in range(len(dic[key])):
            sheet.write(int(key)-1,i+1,dic[key][i])
    w.save('excelFile.xls')
    print "Make xlsx done"



if __name__=='__main__':
    dic=load_txt('student.txt')
    input_info(dic)
~                                
