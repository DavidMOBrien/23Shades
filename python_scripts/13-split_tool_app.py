with open('tool_application.csv', 'r') as inputFile:
    dataset = inputFile.readlines()

    ref = {}

    for item in dataset:
        item = item.strip('\n')
        item = item.split(',')
        
        print(item)

        ref[item[0]] = item[1]

not_found = set()
    
with open('12-sitepackages_removed.txt', 'r') as inputFile:
    dataset = inputFile.readlines()

    for item in dataset:
        item = item.strip('\n')
        splitted = item.split(',')

        if splitted[1] in ref:
            if ref[splitted[1]] == 'Applied':
                with open('13-apps.csv', 'a') as outputFile:
                    outputFile.write(item)
                    outputFile.write('\n')
            else:
                with open('13-tools.csv', 'a') as outputFile:
                    outputFile.write(item)
                    outputFile.write('\n')
        else:
            not_found.add(splitted[1])

for item in not_found:
    print('nooo')