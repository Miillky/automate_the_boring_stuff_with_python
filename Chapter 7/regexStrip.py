import pyperclip, re

def regexStrip(text, characterToStrip = ' '):
    if characterToStrip == ' ':
        return re.compile(r'^\s*|\s*$').sub('', text)
    else:
       return re.compile(str(characterToStrip)).sub('', text)

text = '''  Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argu-
ment to the function will be removed from the string.   '''


print(regexStrip(text))
print(regexStrip(text, characterToStrip='strip'))