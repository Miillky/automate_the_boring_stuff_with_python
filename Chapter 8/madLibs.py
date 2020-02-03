#! python3
# Read txt file and let the user replace nouns, verbs, adverbs and adjectives.
# Usage:
# Enter name of any txt file in the cwd and follow prompts to madlib its content

import re

lib = open('./Chapter 8/madLibs.txt')
string = lib.read()

# Find all madlibable prompt words
replace = 0
madlibRegex = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
matches = madlibRegex.findall(string)

# Replace words
for found in matches:
    sub = str(input('Enter a ' + found + ': '))
    string = string.replace(found, sub, 1)

print(string)