import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen

from pip._vendor import requests

url = 'https://stockx.com/air-jordan-1-retro-high-court-purple-white'

sauce = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(sauce).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

print(soup.title.string)

for average in soup.find_all('div', class_='gauge-title'):
    print(average.text, end="       ")

print(" ")

for price in soup.find_all('div', class_='gauge-value'):
    print(price.text, end="                                ")

for size in soup.find_all('li', class_='select-option active all'):
    print(size, end=" ")









