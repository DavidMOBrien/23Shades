

def getID(sample):
    return sample.split(',')[0]

def getText(sample):
    return sample.split(',')[-2]

with open("3-preprocessed.txt", "r", errors = 'ignore', encoding = 'utf-8') as inputFile:
    dataset = inputFile.readlines()

with open("4-prepared_cc.txt", "w", errors = 'ignore', encoding = 'utf-8') as outputFile:
    for item in dataset:
        outputFile.write(getID(item) + ', ' + getText(item))
        outputFile.write('\n')