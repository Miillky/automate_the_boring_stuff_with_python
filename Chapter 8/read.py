import os

sep = os.path.sep
path = str(os.getcwd()) + sep + 'Chapter 8' + sep

helloFile = open(path + 'hello.txt')
print(helloFile.read())

sonnetFile = open(path + 'sonnet29.txt')
print(sonnetFile.readlines())