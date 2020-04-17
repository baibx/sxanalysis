import requests
from bs4 import BeautifulSoup
from selenium import webdriver

#login
#username = 'kickmoki@gmail.com'
#password = 'Fancydude42!'

#url = 'https://accounts.stockx.com/login?state=g6Fo2SBWQjdGMUtEaG9HQ2xRYWt6Q1M0NWY3M2lFY3U5SnFsYaN0aWTZIG40QWc2R1ppbERMVkRMTHhGdF9ZZHE2OUxXQ2RGam9Go2NpZNkgT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQ&client=OVxrt4VJqTx7LIUKd661W0DuVMpcFByD&protocol=oauth2&audience=gateway.stockx.com&connection=production&redirect_uri=https%3A%2F%2Fstockx.com%2Fcallback%3Fpath%3D%2F&response_type=code&stockx-currency=USD&stockx-default-tab=login&stockx-is-gdpr=&stockx-language=en&stockx-session-id=&stockx-url=https%3A%2F%2Fstockx.com&stockx-user-agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A75.0)%20Gecko%2F20100101%20Firefox%2F75.0'


'''driver.get(url)

import time
time.sleep(2)

login = driver.find_element_by_xpath('//*[@id="email-login"]')
login.click()
login.send_keys(username)

password_send = driver.find_element_by_xpath('//*[@id="password-login"]')
password_send.click()
password_send.send_keys(password)

login_box = driver.find_element_by_xpath('//*[@id="login-button-text"]')
login_box.click()'''

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
print(last_sold.text)

