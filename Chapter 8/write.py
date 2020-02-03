import os

sep = os.path.sep
path = str(os.getcwd()) + sep + 'Chapter 8' + sep

baconFile = open(path + 'bacon.txt', 'w')
baconFile.write('Hello world!\n')

baconFile.close()
baconFile = open(path + 'bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open(path + 'bacon.txt')
content = baconFile.read()
baconFile.close()

print(content)