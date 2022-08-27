import re

def noqa_re(myString):
    if re.search('noqa', myString) or re.search('NOQA', myString):
        return True
    return False

def protocol_re(myString):
    if re.search('generated protocol buffer', myString):
        return True
    return False

def utf8_re(myString):
    if re.search('coding', myString) and (re.search('utf-8', myString) or re.search('utf8', myString)):
        return True
    return False

def usrbinpython_re(myString):
    if re.search('usr', myString) and re.search('bin', myString) and re.search('env', myString) and re.search('python', myString):
        return True
    return False

def license_re(myString):
    if re.search('License', myString) or re.search('license', myString) or re.search('LICENSE', myString):
        print('found')
        return True
    return False

def pylint_re(myString):
    if re.search('pylint:', myString):
        return True
    return False

def test_sample(sample):
    text = sample[-2]

    if noqa_re(text):

        return False

    if protocol_re(text):

        return False

    if utf8_re(text):

        return False

    if usrbinpython_re(text):

        return False

    if license_re(text):

        return False

    if pylint_re(text):

        return False

    return True

with open('7-union.txt', 'r', errors = 'ignore', encoding = 'utf-8') as inputFile:
    dataset = inputFile.readlines()

toWrite = []

for item in dataset:
    if test_sample(item.split(',')):
        toWrite.append(item)

with open('8-autogen_removed_sorted.txt', 'w', errors = 'ignore', encoding = 'utf-8') as outputFile:
    for item in toWrite:
        outputFile.write(item)