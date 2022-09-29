import csv

outFile = open('update.csv', 'w', encoding="ISO-8859-1")

with open('old.csv', 'r', encoding="ISO-8859-1") as t1, open('new.csv', 'r', encoding="ISO-8859-1") as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w', encoding="ISO-8859-1") as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)