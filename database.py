import pymysql
from datetime import datetime

class db():
	def __init__(self,db_name='iot'):
		self.obj=pymysql.connect(host='127.0.0.1', user='root', passwd='',db=db_name)
		self.cur=self.obj.cursor()
		try:
			self.cur.execute('''CREATE TABLE tb(id INTEGER PRIMARY KEY AUTO_INCREMENT, time CHAR(30), status CHAR(30))''')
		except:
			print e
			pass	



	def insert(self,status):
		time=datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
		self.cur.execute('''INSERT INTO tb(time,status) VALUES(%s,%s)''',(time,status))
		self.obj.commit() 

	def fetch(self):
		self.cur.execute('''SELECT time,status FROM tb ORDER BY time DESC LIMIT 1''')
		res=self.cur.fetchall()
		try:
			res = res[0][1].encode('ascii')
		except Exception, e:
			print e
			
		
		return res

