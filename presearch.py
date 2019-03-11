# I just found out about a site called presearch.org which pays you for using
# there search engine. It gives you 8 PRE for total 32 searches and you can withdraw
# after getting 1000 PRE. So this script automates your work by searching 32 times out
# of the attributes provided in the list `inputs`.

# Just provide mail address and password to your account and see the magic happen

from selenium import webdriver
import time
import random
browser = webdriver.Firefox()
browser.get('https://www.presearch.org/login')
email = browser.find_element_by_name('email')
email.send_keys('<your mail address>')
password = browser.find_element_by_name('password')
password.send_keys('<password of your mail address')
password.submit()
time.sleep(5)
inputs = ['quora', 'github', 'gmail', 'facebook', 'instagram', 'swagbucks', 'google', 'gitter']
for i in range(32):
    search = browser.find_element_by_id('search')
    x = random.randint(0, len(inputs)-1)
    search.send_keys(inputs[x])
    search.submit()
    time.sleep(5)
    browser.back()
    time.sleep(2)
browser.refresh()
