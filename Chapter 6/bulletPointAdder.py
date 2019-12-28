#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop throught all indexes in the "lines list"
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = '\n' . join(lines)
pyperclip.copy(text)

"""
Lists of animals
List of aquarium life
List of bilogists by author abbreviation
List of culivars
"""
# Copy lists text and run python bulletPointAdder.py -> clipboard should be the text with stars (*) before each line