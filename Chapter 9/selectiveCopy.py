#! python3
# Walk though a folder tree and copy all files of a particular extension.

import shutil, os

folder = str(input('Enter the absolute filepath of the directory you wish to copy from: '))
extension = str(input("Enter the extension you'd like to copy: "))
destination = str(input("Enter destination folder's absolute filepath: "))

for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('{}'.format(extension)):
            shutil.copy(os.path.join(folders, filename), destination)

print(
        'Selective copying has finished - all files of', extension,
        'type have been copied from', os.path.basename(folder), 'to',
        os.path.basename(destination)
    )