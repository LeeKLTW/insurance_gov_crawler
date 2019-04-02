# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
driver.get('http://ins-info.ib.gov.tw/customer/announceinfo.aspx')

ComapnyType = Select(driver.find_element_by_id("ctl00_MainContent_ddlComapnyType"))

ComapnyType.select_by_visible_text(ComapnyType.options[1].text)
ComapnyName = Select(driver.find_element_by_id("ctl00_MainContent_ddlComapnyName"))

ComapnyName.select_by_visible_text(ComapnyName.options[1].text)

driver.find_element_by_id('ctl00_MainContent_btnQuery').click()

html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')
prefix = 'http://ins-info.ib.gov.tw/customer/'
product_url = prefix+soup.select('#CONTENT > table > tbody > tr > td > table:nth-child(12) > tbody > tr > td > a')[0]['href']
driver.get(product_url)
driver.find_element_by_id('ctl00_MainContent_btnQuery').click()
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

product_code_list = []
product_name_list = []
candidates = soup.select('tbody > tr:nth-child(1) > td:nth-child(1) span')

for i in range(len(candidates) - 2):
    if i % 2 == 0:
        product_code_list.append(candidates[i].text)
    elif i % 2 == 1:
        product_name_list.append(candidates[i].text)

[prefix+a['href'] for a in soup.select('#ctl00_MainContent_dlPaging > tbody > tr > td > a')[1:]]
product_url = [prefix+a['href'] for a in soup.select('#ctl00_MainContent_dlPaging > tbody > tr > td > a')[1:]][0]
driver.get(product_url)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')
candidates = soup.select('tbody > tr:nth-child(1) > td:nth-child(1) span')

for i in range(len(candidates) - 2):
    if i % 2 == 0:
        product_code_list.append(candidates[i].text)
    elif i % 2 == 1:
        product_name_list.append(candidates[i].text)

# 承保範圍, 不保事項, 保單紅利,拒保職業,理賠申請文件