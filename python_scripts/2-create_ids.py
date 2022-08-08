import random
def uniqueid():
    seed = 0
    while True:
        seed = str(seed)

        while len(seed) != 9:
            seed = '0' + seed
        yield seed
        seed = int(seed)
        seed += 1

def numtolet(id):
    ref = {"0":"a", "1" : "b", "2": "c", "3": "d", "4": "e", "5": "f",
            "6": "g", "7": "h", "8": "i", "9": "j"}
    output = ""

    for letter in id:
        output += ref[letter]
    
    return output

unique_sequence = uniqueid()

with open('1-output.txt', 'r', errors = 'ignore', encoding = 'utf-8') as inputFile:
    dataset = inputFile.readlines()

    with open('2-id_output.txt' ,'w', errors = 'ignore', encoding = 'utf-8') as outputFile:
        for num,item in enumerate(dataset):
            if num % 10000 == 0:
                print( str(num+1) + ' / ' + str(len(dataset)))
                
            item = numtolet(str(next(unique_sequence))) + ',' + item

            outputFile.write(item)