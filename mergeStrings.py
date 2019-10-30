import os
from pathlib import Path

def readStrings(fname, dname):
    fpath = os.path.join(dname, fname)
    fileHandler = open (fpath, "r")
    listOfLines = fileHandler.readlines()
    temp = ""
    for s in listOfLines:
        strings.append(s)
    fileHandler.close()
    strings.append(temp)
    

def getAllStrings(folder):
    print("folders: ", end ="")
    for inner in folder: 
        for csv in inner[2]:
            if csv.endswith('.csv'):
                readStrings(csv, inner[0])


logFiles = []
strings = []
files = []
for i in os.walk('.'):
    if(len(i[1])==0):
        files.append(i)
getAllStrings(files)


print('logs:')
print(logFiles)