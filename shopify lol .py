el = "https://nrml.ca/collections/mens-winter-coats/products/m-dptfrd-dwn-jkt-nf0a3mjlg2n"
email = "baibx13137@gmail.com"
first_name = "Baizhen"
last_name = "Wang"
addy = "1840 78th st"
city = "brooklyn"
zipcode = "11214"
phone = "3472956760"

checkout11 = 'http://nrml.ca/checkout'
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(el)

size = driver.find_element_by_xpath('//*[@id="AddToCartForm"]/div[1]/div[2]/div[3]/div[2]')
size.click()

atc = driver.find_element_by_xpath('//*[@id="AddToCart"]')
atc.click()

import time

time.sleep(2)
checkout = driver.get(checkout11)

email1 = driver.find_element_by_xpath('//*[@id="checkout_email"]')
email1.send_keys(email)

first_name1 = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]')
first_name1.send_keys(first_name)

last_name1 = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]')
last_name1.send_keys(last_name)

address1 = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]')
address1.send_keys(addy)

city1 = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]')
city1.send_keys(city)

zip1 = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]')
zip1.send_keys(zipcode)

phone1 = driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]')
phone1.send_keys(phone)














''' usernameBox = driver.find_element_by_xpath('//*[@id="email"]')
usernameBox.send_keys(loginUsername)

passwordBox = driver.find_element_by_xpath('//*[@id="pass"]')
passwordBox.send_keys(loginPassword)

loginBox = driver.find_element_by_xpath('//*[@id="u_0_b"]')
loginBox.click()'''