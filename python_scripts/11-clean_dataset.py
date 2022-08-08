def getRemoveRevision(sample):
    return sample.split(',')[-1][0:-1]

def getID(sample):
    return sample.split(',')[0]

def getRepo(sample):
    return sample.split(',')[1]

def getAddRevision(sample):
    return sample.split(',')[2]

def getFilename(sample):
    return sample.split(',')[3]

def getText(sample):
    return sample.split(',')[4]

with open("10-removed_duplication.txt", "r") as inputFile:
    dataset = inputFile.readlines()

with open("11-cleaned.txt", "w") as outputFile:
    for item in dataset:
        outputFile.write(getID(item) + ',' + getRepo(item) + ',' + getFilename(item) + ',' + getAddRevision(item) + ',' + 
        getRemoveRevision(item) + ',' + getText(item) + '\n')