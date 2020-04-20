import requests
from bs4 import BeautifulSoup
from selenium import webdriver

'''#login
username = 'kickmoki@gmail.com'
password = 'DXChruoyVp'''

#url = 'https://accounts.stockx.com/login?state=g6Fo2SBWQjdGMUtEaG9HQ2xRYWt6Q1M0NWY3M2lFY3U5SnFsYaN0aWTZIG40QWc2R1ppbERMVkRMTHhGdF9ZZHE2OUxXQ2RGam9Go2NpZNkgT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQ&client=OVxrt4VJqTx7LIUKd661W0DuVMpcFByD&protocol=oauth2&audience=gateway.stockx.com&connection=production&redirect_uri=https%3A%2F%2Fstockx.com%2Fcallback%3Fpath%3D%2F&response_type=code&stockx-currency=USD&stockx-default-tab=login&stockx-is-gdpr=&stockx-language=en&stockx-session-id=&stockx-url=https%3A%2F%2Fstockx.com&stockx-user-agent=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A75.0)%20Gecko%2F20100101%20Firefox%2F75.0'
execute = r'C:\Users\baizh\AppData\Local\Programs\Python\Python38-32\geckodriver.exe'

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(executable_path=execute, firefox_options=options)

#driver.get(url)


'''print("Logging in!")
login = driver.find_element_by_xpath('//*[@id="email-login"]')
login.click()
login.send_keys(username)
print("Username Filled!")

print("Sending Password!")
password_send = driver.find_element_by_xpath('//*[@id="password-login"]')
password_send.click()
password_send.send_keys(password)

login_box = driver.find_element_by_xpath('//*[@id="login-button-text"]')
login_box.click()
print("Logged in!")'''

url = 'https://stockx.com/adidas-yeezy-boost-350-v2-butter'
source = requests.get(url)
soup = BeautifulSoup(source.text, 'html.parser')

driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')

last_sold = sel_soup.find('div', class_='col-md-8 product-history')
view_all = last_sold.find('table', class_='latest-sales table table-striped table-condensed')

tr = view_all.find('tr')

print("Getting last sold")

for th in tr.find_all('th'):
    print(th.text, end = "                   ")

print(" ")

for tr in view_all.find('tbody'):

    split = tr.text.split()
    size = split[0].split('$')
    cost = size[1].split('Monday')
    date = split[1] + " " + split[2] + " 2020"
    #print(size[0] + "                     " + '$' + cost[0] + "                     " + date + "           who cares about time")
    print(cost)




driver.quit()
print("Program exited")

#split into two with the year
#upload results to a dictionary
#call the dictionary
#go from there

#split by today's date
#split by dollar sign



