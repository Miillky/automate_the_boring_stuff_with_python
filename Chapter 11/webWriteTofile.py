import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('Chapter 11/RomeoAndJuliet.txt', 'wb') # wb binary mode

for chunk in res.iter_content(1000000):
    playFile.write(chunk)

playFile.close()