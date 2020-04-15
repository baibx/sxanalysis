import bs4 as bs
import requests
from urllib.request import Request, urlopen

url = "https://stockx.com/air-jordan-1-retro-high-court-purple-white"

sauce = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(sauce).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

mobile = soup.find('ul', class_='list-unstyled sneakers')

for size in mobile.find_all('div', class_="inset"):

    size1 = size.find('div', class_="title")
    size_price = size.find('div', class_="subtitle")

    size1 = size1.text
    size_price = size_price.text

    print(size1 + " " + size_price)

    print(" ")




