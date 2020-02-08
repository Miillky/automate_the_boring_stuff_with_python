#! /usr/bin/python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com' # starting url
os.makedirs('./Chapter 11/xkcd', exist_ok=True) # store comics in folder

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = url + comicElem[0].get('src')
        # Download the image
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to xkcd folder
        imageFile = open('./Chapter 11/xkcd/' + os.path.basename(comicUrl), 'wb')
        for chink in res.iter_content(1000000):
            imageFile.write(chink)
        imageFile.close()

    #Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')