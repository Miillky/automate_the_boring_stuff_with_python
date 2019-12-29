import re, pyperclip

passLength = re.compile(r'.{8,}') # >= 8 characters
passUpper = re.compile(r'[A-Z]') # Contains an upper case letter
passLower = re.compile(r'[a-z]') # Contains a lower case letter
passDigit = re.compile(r'[0-9]') # Contains a digit

def checkPasswordStrength(password):
    if passLength.search(password) is None:
        return False
    elif passUpper.search(password) is None:
        return False
    elif passLower.search(password) is None:
        return False
    elif passDigit.search(password) is None:
        return False
    else:
        return True

password = str(pyperclip.paste())

if checkPasswordStrength(password) == True:
    print('Strong password.')
else:
    print('Weak password.')

# Or
if re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$').search(password):
    print('Strong password.')
else:
    print('Weak password.')