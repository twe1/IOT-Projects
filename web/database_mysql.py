import pymysql
from datetime import datetime

class database():
	def __init__(self):
		self.obj=pymysql.connect(host='127.0.0.1', user='root', passwd='',db='iot')
		self.cur=self.obj.cursor()
		try:
			self.cur.execute('''CREATE TABLE tb(id INTEGER PRIMARY KEY AUTOINCREMENT, time STRING, status STRING)''')
		except:
			pass	

		
	def insert(self,status):
		time=datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
		self.cur.execute('''INSERT INTO tb(time,status) VALUES(%s,%s)''',(time,status))
		self.obj.commit() 

dbObj = database()

