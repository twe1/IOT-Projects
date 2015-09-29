import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='',db='iot')
cur = conn.cursor()


def table_create():
    cur.execute('CREATE TABLE tb (id INTEGER NOT NULL AUTO_INCREMENT,\
     time VARCHAR(25),\
     status VARCHAR(5),\
     PRIMARY KEY (id))')

table_create()