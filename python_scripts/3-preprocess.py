

def test_sample(sample):
    text = sample[-2]

    if len(text) < 2:

        return False

    return True


with open('2-id_output.txt', 'r', errors = 'ignore', encoding = 'utf-8') as inputFile:
    dataset = inputFile.readlines()

for num,item in enumerate(dataset):

    if num % 1000 == 0:
        print(num)

    if test_sample(item.split(',')):
        with open('3-preprocessed.txt', 'a', errors = 'ignore', encoding = 'utf-8') as outputFile:
            outputFile.write(item)