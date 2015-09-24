import sqlite3
from datetime import datetime

class db():
	def __init__(self,db_name="rpi.db"):
		self.obj=sqlite3.connect(db_name,check_same_thread=False)
		self.cur=self.obj.cursor()
		try:
			self.cur.execute('''CREATE TABLE tb(id INTEGER PRIMARY KEY AUTOINCREMENT, time STRING, status STRING)''')
		except:
			pass	


	def create_table(self):
		self.cur.execute('''CREATE TABLE tb(id INTEGER PRIMARY KEY AUTOINCREMENT, time STRING, status STRING)''')

	def insert(self,status):
		time=datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
		self.cur.execute('''INSERT INTO tb(time,status) VALUES(?,?)''',(time,status))
		self.obj.commit() 

	def fetch(self):
		self.cur.execute('''SELECT time,status FROM tb ORDER BY time DESC LIMIT 1''')
		res=self.cur.fetchall()
		try:
			res = res[0][1].encode('ascii')
		except Exception, e:
			print e
			
		
		return res

