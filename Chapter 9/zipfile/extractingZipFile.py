import zipfile, os
os.chdir('./Chapter 9/zipfile')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()