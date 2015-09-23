import sqlite3
from datetime import datetime

class db():
	def __init__(self,db_name="database.db"):
		self.obj=sqlite3.connect(db_name,check_same_thread=False)
		self.cur=self.obj.cursor()
		try:
			self.cur.execute('''CREATE TABLE tb(id INTEGER PRIMARY KEY AUTOINCREMENT, time STRING, cmd STRING)''')
		except:
			pass	


	def create_table(self):
		self.cur.execute('''CREATE TABLE tb(id INTEGER PRIMARY KEY AUTOINCREMENT, time STRING, cmd STRING)''')

	def insert(self,cmd):
		time=datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")
		self.cur.execute('''INSERT INTO tb(time,cmd) VALUES(?,?)''',(time,cmd))
		self.obj.commit() 

	def fetch(self):
		self.cur.execute('''SELECT time,cmd FROM tb ORDER BY time DESC LIMIT 1''')
		res=self.cur.fetchall()
		res = res[0][1].encode('ascii')
		return res

