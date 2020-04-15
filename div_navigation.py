import bs4 as bs
import requests
from urllib.request import Request, urlopen

url = "https://stockx.com/air-jordan-1-retro-high-court-purple-white"

sauce = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(sauce).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

mobile = soup.find('ul', class_='list-unstyled sneakers')

print(mobile.text)