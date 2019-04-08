# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
from models import conn_sqlite
import logging

logging.basicConfig(level=logging.INFO, format="[%(levelname)-8s] - %(asctime)s - PID %(process)d - %(message)s")

PREFIX = "http://ins-info.ib.gov.tw/customer/"


def crawl_products(company):
    # product
    driver.find_element_by_css_selector(
        '#contentbox > div.title > table > tbody > tr > td > table > tbody > tr > th > center > input').click()

    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    candidates = soup.select('tbody > tr:nth-child(1) > td:nth-child(1) span')
    product_code_list = []
    product_name_list = []

    for i in range(len(candidates) - 2):
        if i % 2 == 0:
            product_code_list.append(candidates[i].text)
        elif i % 2 == 1:
            product_name_list.append(candidates[i].text)

    conn, cur = conn_sqlite()

    id_, name, company = 'testid', 'testname', 'testcompany'

    sql = """
    IF NOT EXISTS (SELECT * FROM insurance_product WHERE product_id=?)
        BEGIN
            INSERT INTO insurance_product (product_id,product_name,company) VALUES (?,?,?)
        End
    """
    # sql = "INSERT INTO insurance_product (product_id,product_name,company) VALUES (?,?,?);"
    cur.execute(sql, (id_,id_, name, company,))
    conn.commit()

    for id_, name in zip(product_code_list, product_name_list):
        try:
            # print(sql)
            # cur.execute(sql, (id_,id_, name, company,))
            cur.execute(sql, (id_, name, company,))
            conn.commit()
        except:
            print(id_)


    next_page = soup.select(
        "#contentbox > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td:nth-child(3) a")[
        0].get('href')

    if next_page is None:
        return
    else:
        next_page = PREFIX + next_page
        driver.get(next_page)
        crawl_products(company)
    return


def clist_2_plist(company):
    driver.get(PREFIX + 'announceinfo.aspx')

    ComapnyType = Select(driver.find_element_by_id("ctl00_MainContent_ddlComapnyType"))
    ComapnyType.select_by_visible_text(life_insurance)

    ComapnyName = Select(driver.find_element_by_id("ctl00_MainContent_ddlComapnyName"))
    ComapnyName.select_by_visible_text(company)
    driver.find_element_by_css_selector(
        '#contentbox > table > tbody > tr > td > table > tbody > tr:nth-child(3) > td > input').click()
    driver.find_element_by_css_selector(
        '#CONTENT > table > tbody > tr > td > table:nth-child(12) > tbody > tr > td > a').click()
    return


def main():
    global driver
    global life_insurance
    driver = webdriver.Chrome('./chromedriver')
    driver.get(PREFIX + 'announceinfo.aspx')

    ComapnyType = Select(driver.find_element_by_id("ctl00_MainContent_ddlComapnyType"))
    life_insurance = ComapnyType.options[1].text
    ComapnyType.select_by_visible_text(life_insurance)

    ComapnyName = Select(driver.find_element_by_id("ctl00_MainContent_ddlComapnyName"))
    companys_list = [c.text for c in ComapnyName.options[1:]]

    for company in companys_list:
        clist_2_plist(company)
        crawl_products(company)


if __name__ == '__main__':
    main()
