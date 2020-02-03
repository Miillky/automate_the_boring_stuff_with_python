#! python3
import os, re

files = os.listdir('./Chapter 8')
textFiles = []

txtRegex = re.compile(r'.txt')

for doc in files:
    if txtRegex.search(doc) is not None:
        textFiles.append(doc)

# Write regex to match
searchRegex = re.compile(r'\s?\w*\!') # Matches all words ending in !

for doc in textFiles:
    openFile = open('./Chapter 8/{0}'.format(doc))
    contents = openFile.read()
    string = ''.join(contents)
    found = searchRegex.findall(string)
    foundString = ' '.join(found)
    print(foundString)