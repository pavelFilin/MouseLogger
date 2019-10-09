import os
from pathlib import Path

files = os.listdir('.')

path=str(os.path.dirname(os.path.abspath(__file__))).split('\\')
print(path[len(path)-1])


logs = [i for i in files if i.endswith('.csv')]

for log in logs:
    print("files: ", end="")
    print("\t{0}".format(log))

print()


right = 0
left = 0

for log in logs:
    fileHandler = open (log, "r")
    listOfLines = fileHandler.readlines()
    for s in listOfLines:
        x = s.split(",")
        if x[0] == "Button.left":
            left = left+1
        if x[0] == "Button.right":
            right = right + 1
    fileHandler.close()

print('left\t {0}'.format(left))
print('right\t{0}'.format(right))
print('all\t{0}'.format(left+right))
input('....')