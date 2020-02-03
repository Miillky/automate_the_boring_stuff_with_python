import shelve
import os

sep = os.path.sep
path = str(os.getcwd()) + sep + 'Chapter 8' + sep

shelfFile = shelve.open(path + 'mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open(path + 'mydata')
print(type(shelfFile))

print(shelfFile['cats'])
shelfFile.close()

shelfFile = shelve.open(path + 'mydata')
print(shelfFile.keys())
print(list(shelfFile.values()))
shelfFile.close()