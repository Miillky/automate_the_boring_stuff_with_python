#! /usr/bin/python3
# lucky.py - Open several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...') # display text while downloading the Google page

link = 'https://www.google.com/search?q=' + ' '.join(sys.argv[1:])
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
res = requests.get(link, headers=headers)
res.raise_for_status()

# Retrive top search result link
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each resutl.
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))