# Handling files
import os
inputFile= open('lyrics.txt','r')
outputFile = open('copylyrics.txt','w')
for line in inputFile:
    outputFile.write(line)
    print (line,end = '')
   
inputFile.close() 
outputFile.close()
os.remove('copylyrics.txt')
# both opening and writing files should be in same folder

