# encoding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from models import conn_mysql
import logging

logging.basicConfig(level=logging.INFO,
                    format="[%(levelname)-8s] - %(asctime)s - PID %(process)d - %(message)s")

PREFIX = "http://ins-info.ib.gov.tw/customer/"


class InsuranceProduct:
    def __init__(self, product_id, product_name, company, coverage_brief=None, coverage=None,
                 exception=None,
                 exception_brief=None, dividend=None, rejection=None, claim_app_doc=None):
        self.product_id = product_id
        self.product_name = product_name
        self.company = company
        self.coverage_brief = coverage_brief
        self.coverage = coverage
        self.exception = exception
        self.exception_brief = exception_brief
        self.dividend = dividend
        self.rejection = rejection
        self.claim_app_doc = claim_app_doc


def clist_to_ppage(company):
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


def iter_products(company):
    # product
    driver.find_element_by_css_selector(
        '#contentbox > div.title > table > tbody > tr > td > table > tbody > tr > th > center > input').click()

    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    candidates = soup.select('tbody > tr > td:nth-child(1) span')
    product_page_url = driver.current_url

    def _write_product_detail(i):
        p = InsuranceProduct(product_id=candidates[i - 1], product_name=candidates[i],
                             company=company)

        idx = int(i // 2)
        idx_html = f"#ctl00_MainContent_DataGridSearchResults > tbody > tr:nth-child({idx}) > td:nth-child(3) >select"
        term_opt = Select(driver.find_element_by_css_selector(idx_html))
        coverage_visible = [i.text for i in term_opt.options if '承保' in i.text][0]
        dividend_visible = [i.text for i in term_opt.options if '紅利' in i.text][0]
        rejection_visible = [i.text for i in term_opt.options if '職業' in i.text][0]
        claim_app_doc_visible = [i.text for i in term_opt.options if '文件' in i.text][0]

        def _call_back():
            driver.get(product_page_url)
            driver.find_element_by_css_selector(
                '#contentbox > div.title > table > tbody > tr > td > table > tbody > tr > th > center > input').click()
            term_opt = Select(driver.find_element_by_css_selector(idx_html))
            return term_opt

        term_opt = _call_back()
        term_opt.select_by_visible_text(coverage_visible)

        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')

        coverage_li = [i.text.replace(' ', '').replace('\n', '') for i in
                       soup.select(
                           "#contentbox > div > table:nth-child(6) > tbody > tr > td:nth-child(2)")][
                      1:]
        coverage_b_li = [i.text.replace(' ', '').replace('\n', '') for i in
                         soup.select(
                             "#contentbox > div > table:nth-child(6) > tbody > tr > td:nth-child(1)")][
                        1:]
        exception_li = [i.text.replace(' ', '').replace('\n', '') for i in
                        soup.select(
                            "#contentbox > div > table:nth-child(8) > tbody > tr > td:nth-child(2)")][
                       1:]
        exception_b_li = [i.text.replace(' ', '').replace('\n', '') for i in
                          soup.select(
                              "#contentbox > div > table:nth-child(8) > tbody > tr > td:nth-child(1)")][
                         1:]

        p = InsuranceProduct(product_id='202391RZ9DGE021A11Z10000007',
                             product_name='台灣人壽一年期二至十一級失能健康保險附約',
                             company=company)

        p.coverage = '/'.join(coverage_li)
        p.coverage_brief = '/'.join(coverage_b_li)
        p.exception = '/'.join(exception_li)
        p.exception_brief = '/'.join(exception_b_li)

        term_opt = _call_back()
        term_opt.select_by_visible_text(dividend_visible)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        dividend_li = [i.text.replace(' ', '').replace('\n', '') for i in
                       soup.select("#contentbox > table > tbody > tr > td:nth-child(2)")][3:]
        p.dividend = '/'.join(dividend_li)

        term_opt = _call_back()
        term_opt.select_by_visible_text(rejection_visible)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        li1 = [i.text.replace(' ', '').replace('\n', '') for i in
               soup.select("#contentbox > div > table > tbody > tr > td:nth-child(1)")][3:]
        li2 = [i.text.replace(' ', '').replace('\n', '') for i in
               soup.select("#contentbox > div > table > tbody > tr > td:nth-child(2)")][3:]
        rejection_li = []
        for i, j in zip(li1, li2):
            rejection_li.append(str(i) + ": " + str(j))
        p.rejection = '/'.join(rejection_li)

        term_opt = _call_back()
        term_opt.select_by_visible_text(claim_app_doc_visible)
        html_source = driver.page_source
        soup = BeautifulSoup(html_source, 'html.parser')
        li1 = [i.text.replace(' ', '').replace('\n', '') for i in
               soup.select("#contentbox > div > table > tbody > tr > td:nth-child(1)")][3:]
        li2 = [i.text.replace(' ', '').replace('\n', '') for i in
               soup.select("#contentbox > div > table > tbody > tr > td:nth-child(2)")][3:]
        claim_app_doc_li = []
        for i, j in zip(li1, li2):
            claim_app_doc_li.append(str(i) + ": " + str(j))
        p.claim_app_doc = '/'.join(rejection_li)

        sql = """
        INSERT INTO insurance_product 
        (product_id,product_name,company,coverage_brief,coverage,exception,exception_brief,dividend,rejection,claim_app_doc)
        SELECT ?,?,?,?,?,?,?,?,?,?
        WHERE NOT EXISTS(SELECT * FROM insurance_product WHERE product_id=?);
        """

        conn, cur = conn_mysql()
        cur.execute(sql, (
            p.product_id, p.product_name, p.company, p.coverage_brief, p.coverage, p.exception,
            p.exception_brief,
            p.dividend, p.rejection, p.claim_app_doc, p.product_id))
        conn.commit()
        conn.close()

    for i in range(2, len(candidates) - 2, 2):
        _write_product_detail(i)

    next_page = soup.select(
        "#contentbox > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td:nth-child(3) a")[
        0].get('href')

    if next_page is None:
        return
    else:
        next_page = PREFIX + next_page
        driver.get(next_page)
        iter_products(company)
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
        try:
            clist_to_ppage(company)
            iter_products(company)
        except:
            print('Cannot get', company)  # e.g. '國華人壽保險股份有限公司'

    driver.close()


if __name__ == '__main__':
    main()
