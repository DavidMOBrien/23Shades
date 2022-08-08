#below are all helper functions to abstract away how info is retrieved
def getType(sample):
    return sample.split(',')[-1]

def getID(sample):
    return sample.split(',')[0]

def getRepo(sample):
    return sample.split(',')[1]

def getRevID(sample):
    return sample.split(',')[2]

def getFilename(sample):
    return sample.split(',')[3]

def getText(sample):
    return sample.split(',')[4]


def isRemoval(item, compare):
    if getType(compare) != 'DELETED\n':
        #print('failed type')
        return False
    if getFilename(item) != getFilename(compare):
        #print('failed filename')
        return False
    if getText(item) != getText(compare):
        #print('failed text')
        return False
    return True



with open('8-autogen_removed_sorted.csv', 'r') as inputFile:
    dataset = inputFile.readlines()

#just for logging purposes
limit = str(len(dataset))



for num,item in enumerate(dataset):
 

    #logging purposes
    if num % 1000 == 0:
        print(str(num+1) + ' / ' + limit)

    #removes newline char
    item = item.strip('\n')

    #check if an item is an introduction, if it is, we want to search through all changes in the current repo to find a removal to link it with
    if getType(item) == 'ADDED':
        
        canEnd = False
        counter = num
        currentRepo = getRepo(item)
        
        while not canEnd:

            #if we go through all of the changes in repo without
            #finding a deletion, then we know this comment must still exist in our system.
            if getRepo(dataset[counter]) != currentRepo:
                with open('9-link_output.txt', 'a') as outputFile:
                    outputFile.write(item + ',' + 'STILL_EXISTS' + '\n')
                canEnd = True

            #call helper function
            if isRemoval(item, dataset[counter]):
                #print('found!')
                #write to output file, then break out of this loop because we have a linking for this current comment.
                with open('9-link_output.txt', 'a') as outputFile:
                    outputFile.write(item + ',' + getRevID(dataset[counter]) + '\n')
                canEnd = True


            counter += 1

            if counter == len(dataset):
                canEnd = True

        

        