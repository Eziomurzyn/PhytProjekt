#!/usr/bin/env python

#import subprocess

dirStr = '''K1
    K2
    K3
        K4
    K5
        K6'''
folderList=[]
tabulation=0;
lastTab=0;
foldername = ""
first = True
for i in dirStr:
    if(i==' '):
        if(foldername!=""):
            folderList.append(foldername)
        tabulation+=1
        foldername=""
        first=True
    elif(i!='\n'):
        if(tabulation/4 <lastTab and first):
            folderList.append(-1)
            lastTab=tabulation/4
            tabulation=0
        if(tabulation/4 >lastTab and first):
            folderList.append(1)
            lastTab=tabulation/4
            tabulation=0
        foldername+=i
        first=False
        
foldername=""
for i in folderList:
         
     
