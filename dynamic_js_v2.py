import requests
from bs4 import BeautifulSoup
from selenium import webdriver

execute = r'C:\Users\baizh\AppData\Local\Programs\Python\Python38-32\geckodriver.exe'
options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path=execute, firefox_options=options)
url = 'https://stockx.com/air-jordan-1-retro-high-court-purple-white'
source = requests.get(url)
soup = BeautifulSoup(source.text, 'html.parser')

driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')

last_sold = sel_soup.find('div', class_='col-md-8 product-history')
view_all = last_sold.find('table', class_='latest-sales table table-striped table-condensed')

tr = view_all.find('tr')

for th in tr.find_all('th'):
    print(th.text, end = "                   ")

print(" ")

for tr in view_all.find('tbody'):
    split = tr.text
    print(split)

#split into two with the year
#upload results to a dictionary
#call the dictionary
#go from there



