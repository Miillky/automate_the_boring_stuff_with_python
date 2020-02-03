#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage:
# py.exe mcb.pyw save <keyword> - Save clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
# py.exe mcb.pyw delete_all - Deletes all keywords from clipboard

# Works only on Windows

import shelve, pyperclip, sys

mcbShelf = shelve.open('./Chapter 8/mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
# Delete keyword and associated content
elif len(sys.argv) == 2 and sys.argv[1].lower() != 'delete':
    del mcbShelf[sys.argv[2]]
    print([sys.argv[2] + ' deleted'])
elif len(sys.argv) == 2 and sys.arv[1].lower() != 'delete_all':
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print('That keyword doesn\t exist - so nothing has been loaded to the clipboard')

# Clear all shelved entries
elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete_all':
    mcbShelf.clear()
    print('All keywords and asscoiated contents have been deleted')

mcbShelf.close()