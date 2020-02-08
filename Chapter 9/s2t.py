import send2trash

baconFile = open('./Chapter 9/bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

send2trash.send2trash('./Chapter 9/bacon.txt')