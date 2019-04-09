# encoding: utf-8
import sqlite3
import pymysql
import json

def conn_sqlite():
    conn = sqlite3.connect('InsuranceProduct.db')
    cur = conn.cursor()
    return conn, cur


def conn_mysql():
    s = open('acc.json', 'r').readlines()[0]
    s = json.loads(s)

    conn = pymysql.Connection(**s['database'],charset='utf8')  # utf8 to correct encoding
    cur = conn.cursor()

    database = s['database']['database']
    cur.execute(f'USE {database};')
    cur = conn.cursor()
    return conn, cur

def _create_table_insurance_product(cur):
    cur.execute(""" CREATE TABLE insurance_product(
    product_id     VARCHAR(64) NOT NULL,
    product_name   TEXT,
    company TEXT,
    coverage_brief TEXT,
    coverage       TEXT,
    exception      TEXT,
    exception_brief TEXT,
    dividend       TEXT,
    rejection      TEXT,
    claim_app_doc  TEXT,
    PRIMARY KEY (product_id));""")
    return