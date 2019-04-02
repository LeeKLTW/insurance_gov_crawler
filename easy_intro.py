# encoding: utf-8
from selenium import webdriver
import time

driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
res1 = driver.find_element_by_id("content").text
print('Before waiting 3 seconds you get:',res1)

time.sleep(3)
res2 = driver.find_element_by_id("content").text
print('After waiting 3 seconds you get:',res2)

driver.close()