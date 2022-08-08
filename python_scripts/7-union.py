def getID(comment):
    return comment[0:9]

def format(data):
    return data[0:10] + data[26:]

with open("2-id_output.txt", "r", errors = 'ignore', encoding = 'utf-8') as inputFile:
    ref_dataset = inputFile.readlines()

    referral = {}

    for item in ref_dataset:
        referral[getID(item)] = item

    del ref_dataset

print("done with referral")

with open("6-keyword_output.txt", "r", errors = 'ignore', encoding = 'utf-8') as inputFile:
    key_dataset = inputFile.readlines()

    key_set = set()

    for item in key_dataset:
        key_set.add(getID(item))

    del key_dataset

print("done with keywords")

with open("5-cc_output.txt", "r", errors = 'ignore', encoding = 'utf-8') as inputFile:
    comm_dataset = inputFile.readlines()

    comm_set = set()

    for item in comm_dataset:
        comm_set.add(getID(item))

    del comm_dataset

print("done with comments")

combined = key_set.union(comm_set)

print("done combining")

with open("7-union.txt", "w", errors = 'ignore', encoding = 'utf-8') as outputFile:
    for item in combined:
        outputFile.write(format(referral[item]))