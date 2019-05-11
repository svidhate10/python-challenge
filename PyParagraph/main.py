# -*- coding: utf-8 -*-
"""
Created on Fri May 10 22:26:58 2019

@author: Shubha
"""

import re
import os

#making list of files so we can work it on at a time
list_of_files = ["paragraph_1.txt","paragraph_2.txt"]
for files in list_of_files:
    txtpath = os.path.join("..\\..", 'RUTJC201904DATA3','hw',"week3","ExtraContent","Instructions","PyParagraph","raw_data",files)
    with open(txtpath, 'r') as text:   
        lines = text.read()
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', lines)
        words = re.split(r' ', lines)                    
        letterCount = 0
        for word in words:
            letterCount = letterCount + len(word)
        # Path for Output Files
        outputpath = os.path.join("..\\..","python-challenge","PyParagraph",files.split(".")[0] + "_result.txt")

        lines = []
    
        #Opening outputfile to write summery
        outputfile = open(outputpath, "w")
    
        lines.append("Paragraph Analysis")
        lines.append("-----------------")
        lines.append("Approximate Word Count:: "+str(len(words)))
        lines.append("Approximate Sentence Count: "+str(len(sentences)))
        lines.append("Average letter count: "+ str(round(letterCount/len(words),2)))
        lines.append("Average Sentence Length: "+ str(round(len(words)/len(sentences),2)))
        for line in lines:
            print(line)
            print(line,file=outputfile)
        print()
        #Closing output file
        outputfile.close()