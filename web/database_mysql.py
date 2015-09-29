import pymysql
from datetime import datetime

class database():
	def __init__(self):
		self.conn=pymysql.connect(host='127.0.0.1', user='root', passwd='',db='iot')
		self.cur=self.conn.cursor()
		
	def insert(self,status):
		time=datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
		self.cur.execute('''INSERT INTO tb(time,status) VALUES(%s,%s)''',(time,status))
		self.conn.commit() 

dbObj = database()

