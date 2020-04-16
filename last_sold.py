import bs4 as bs
from selenium import webdriver
from urllib.request import Request, urlopen

url = "https://stockx.com/air-jordan-1-retro-high-court-purple-white"

driver = webdriver.Chrome()
driver.get(url)

content_element = driver.find_element_by_class_name('latest-sales-container')
content_html = content_element.get_attribute("innerHTML")

from bs4 import BeautifulSoup

soup = BeautifulSoup(content_html, "html.parser")

last_sold = soup.find('table', class_='activity-table table table-condensed table-striped ')



for tr in last_sold.find_all('tr'):
    print(tr.prettify)
driver.close()




'''sauce = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(sauce).read()
soup = bs.BeautifulSoup(webpage, 'lxml')

last_sold = soup.find('div', class_='latest-sales-container')

table = last_sold.find('table', class_='activity-table table table-condensed table-striped ')

print(table)'''



