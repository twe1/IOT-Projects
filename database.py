import pymysql
from datetime import datetime

class db():
	def __init__(self,db_name):
		self.db_name = db_name
		self.obj=pymysql.connect(host='127.0.0.1', user='root', passwd='',db=self.db_name)
		self.cur=self.obj.cursor()
		try:
			self.cur.execute('''CREATE TABLE tb(id INTEGER PRIMARY KEY AUTO_INCREMENT, time CHAR(30), status CHAR(30))''')
		except Exception as e:
			print e
			pass	



	def insert(self,status):
		self.obj=pymysql.connect(host='127.0.0.1', user='root', passwd='',db=self.db_name)
		self.cur=self.obj.cursor()

		time=datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
		self.cur.execute('''INSERT INTO tb(time,status) VALUES(%s,%s)''',(time,status))
		self.obj.commit() 
		self.cur.close()

	def fetch(self):
		self.obj=pymysql.connect(host='127.0.0.1', user='root', passwd='',db=self.db_name)
		self.cur=self.obj.cursor()

		self.cur.execute('''SELECT time,status FROM tb ORDER BY time DESC LIMIT 1''')
		res=self.cur.fetchone()
		try:
			res = res[1]
		except Exception, e:
			print e
			
		self.cur.close()
		return res

