# import requests, bs4

# res = requests.get('http://nostarch.com')
# res.raise_for_status()

# noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')
# print(type(noStarchSoup))

import bs4

exampleFile = open('./Chapter 11/example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html5lib')

elems = exampleSoup.select('#author')

print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(str(elems[0].attrs))

pElems = exampleSoup.select('p')
print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
print(str(pElems[2]))
print(pElems[2].getText())

soup = bs4.BeautifulSoup(open('./Chapter 11/example.html'), 'html5lib')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_attr') == None)
print(spanElem.attrs)