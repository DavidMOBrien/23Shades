keywords = ['hack', 'workaround', 'yuck', 'kludge', 'stupidity', 'needed', 'columns', 'unused', 'wtf', 'todo'
        'implementation', 'fixme', 'xxx', 'ends', 'convention', 'configurable', 'apparently', 'fudging']

            
punctuation= '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

with open('3-preprocessed.txt', 'r', errors = 'ignore', encoding = 'utf-8') as inputFile:
    dataset = inputFile.readlines()

for num, item in enumerate(dataset):

    if num % 1000 == 0:
        print(num)

    text = item.split(',')[-2]
    text = text.lower()

    for punc in punctuation:
        text = text.replace(punc, ' ')

    text_split = text.split()

    for key in keywords:
        if key in text_split:
            with open('6-keyword_output.txt', 'a', errors = 'ignore', encoding = 'utf-8') as outputFile:
                outputFile.write(item)
            break