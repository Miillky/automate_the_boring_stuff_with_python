#!/usr/bin python3

"""Download all linked pages from a given URL and note any 404's."""

import requests
import bs4

url = input('Enter the URL that you would like to verify the links for: ')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')
fof = []   # List of links that lead to a 404 page

for link in links:
    try:
        link = link['href']
        if link.startswith('http'):
            checkLink = link
        elif link.startswith('//'):
            checkLink = 'https:' + link
        elif link.startswith('#'):
            checkLink = url + link

        result = requests.get(checkLink)

        if result.status_code == 404:
            fof.append(checkLink)

    except:
        pass

if len(fof) > 0:
    print('Links processed these ' + str(len(fof)) + ' returned error 404:')
    print('\n'.join(fof))
else:
    print('No 404 error links.')