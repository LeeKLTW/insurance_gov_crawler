# encoding: utf-8
import sqlite3
import pymysql


def conn_sqlite():
    conn = sqlite3.connect('InsuranceProduct.db')
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

