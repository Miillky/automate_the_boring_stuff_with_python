#! python3
# pw.py - An insecure password locker program.
# Usage - python pw.py email or python pw.py blog or python pw.py luggage

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2: # checks commands split in spaces python pw.py is one space so its stops, with addtitional command of email, blog or luggage it runs
    print('Usage: python.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + 'copied to clipoard.')
else:
    print('There is no account named ' + account)