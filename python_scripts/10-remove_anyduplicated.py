with open('9-link_output.txt', 'r') as inputFile:
    dataset = inputFile.readlines()

output = []
compare = []
limit = str(len(dataset))

for item in dataset:
    compare.append(item[10:])

for num,item in enumerate(dataset):
    if num % 1000 == 0:
        print(str(num) + ' / ' + limit)
    
    if compare.count(item[10:]) == 1:
        output.append(item)

with open('10-removed_duplication.txt', 'w') as outputFile:
    print("WRITING OUTPUT")
    for item in output:
        outputFile.write(item)