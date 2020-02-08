#! /usr/bin/python3
# mapIt.py - Launches a map in the browser using an adress from the comand line or lipboard
# command line entering -> mapIt 870 Valencia St, San Francisco, CA 94110 -> ['mapIt.py', '870', 'Valencia', 'St, ', 'San', 'Francisco, ', 'CA', '94110']

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get adress form command line.
    address = ' '.join(sys.argv[1:]) # argv[1:] chops off the first element of array
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)