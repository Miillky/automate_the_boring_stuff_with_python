import zipfile
newZip = zipfile.ZipFile('./Chapter 9/zipfile/new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()