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
product_url = prefix + soup.select('#CONTENT > table > tbody > tr > td > table:nth-child(12) > tbody > tr > td > a')[0][
    'href']
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

product_url = [prefix + a['href'] for a in soup.select('#ctl00_MainContent_dlPaging > tbody > tr > td > a')[1:]][0]
driver.get(product_url)
html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')
candidates = soup.select('tbody > tr:nth-child(1) > td:nth-child(1) span')


for i in range(len(candidates) - 2):
    if i % 2 == 0:
        product_code_list.append(candidates[i].text)
    elif i % 2 == 1:
        product_name_list.append(candidates[i].text)


driver.find_element_by_css_selector("#func").click()
driver.find_element_by_css_selector("#func > option:nth-child(3)").click()

html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

table_title = soup.select("#contentbox > div > table:nth-child(6) > tbody > tr:nth-child(1) > td:nth-child(1)")[0].text
if '承保' in table_title:
    coverage_brief = '/'.join([e.text for e in soup.select("#contentbox > div > table:nth-child(6) > tbody > tr > td:nth-child(1) > pre")])
    coverage = '/'.join([e.text for e in soup.select("#contentbox > div > table:nth-child(6) > tbody > tr > td:nth-child(2) > pre")])

table_title =soup.select("#contentbox > div > table:nth-child(8) > tbody > tr:nth-child(1) > td:nth-child(1)")[0].text
if ('不保' in table_title) or ('除外' in table_title):
    # todo exception v.s. exclusion
    exception = '/'.join([e.text for e in soup.select("#contentbox > div > table:nth-child(8) > tbody > tr > td:nth-child(2) > pre")])

driver.get(product_url)




driver.find_element_by_id("ctl00_MainContent_DataGridSearchResults > tbody > tr:nth-child(1) > td:nth-child(3)")
product_info = driver.find_element_by_css_selector("ctl00_MainContent_DataGridSearchResults > tbody > tr:nth-child > td:nth-child")
product_info = driver.find_element_by_id("func")
product_info.__dict__
dir(product_info)
soup.select("tbody tr  td")
soup.select("#ctl00_MainContent_DataGridSearchResults > tbody > tr > td")
"#ctl00_MainContent_DataGridSearchResults > tbody > tr"



"#func"
def crawl():
    pass


def store():
    pass


def main():
    crawl()
    store()


if __name__ == '__main__':
    main()
