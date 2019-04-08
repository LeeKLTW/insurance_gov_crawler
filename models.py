# encoding: utf-8
import sqlite3

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
#
#
# conn, cur = conn_sqlite()
# sql = """CREATE TABLE trip(
# trip_id INT NOT NULL AUTO_INCREMENT,
# user VARCHAR(64) NOT NULL,
# country VARCHAR(64),
# PRIMARY KEY (trip_id));"""
# cur.execute(sql)
# sql = "DROP TABLE trip;"
# cur.execute(sql)
# conn.commit()
#
# trip_li = [('tony','US'),('tony','HK'),('kelly','US')]
#
# for t in trip_li:
#     sql = """INSERT INTO `trip`(`user`,`country`) VALUES(?,?)"""
#     cur.execute(sql,(t[0],t[1]))
#     conn.commit()
#
#
#
#
#
# sql = """
# IF NOT EXISTS (SELECT * FROM trip WHERE user='shelly')
# BEGIN
#     INSERT INTO `trip`(`user`,`country`) VALUES('shelly','UK')
# END
# """
#
# sql = """
# INSERT OR IGNORE INTO `trip`(`user`,`country`) VALUES ('shelly','UK')
# UPDATE `trip` SET country='UK' WHERE user = 'shelly';
# """
#
# sql = """
# INSERT INTO `trip`(`user`,`country`)
# SELECT 'shelly','UK'
# WHERE NOT EXISTS(SELECT * FROM `trip` WHERE `user`='shelly');
# """
#
# cur.execute(sql)
#
# conn.commit()
#
#
#
#
# cur.execute("SELECT * FROM `trip`;")
# cur.execute("""SELECT * FROM `trip` WHERE `user` = "tony" AND `country` = "US" LIMIT 1""")
# res = cur.fetchall()
# print(res)
