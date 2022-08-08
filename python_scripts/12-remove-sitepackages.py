with open('11-cleaned.txt', 'r') as inputFile:
    dataset = inputFile.readlines()



toWrite = []
for item in dataset:
    temp = item.split(',')

    if 'site-packages' not in temp[2]:
        toWrite.append(item)

with open('12-sitepackages_removed.txt', 'w') as outputFile:
    for item in toWrite:
        outputFile.write(item)