
import paho.mqtt.client as mqtt
import threading 
import led
import time
from database import db

client=mqtt.Client()  # Global declaration
db_obj=db()

def on_connect(client,userdata,rc):
	print "\nNode Connected to broker. rc=%d\n\n" %(rc)
	client.subscribe("wa/thread2/publish")

def on_message(client,userdata,msg):
	cmd1=msg.payload              # cmd1 is a live command(might be out of order)
	db_obj.insert(cmd1)
	cmdx=db_obj.fetch()				#cmdx is fetched from db order by time
	if cmdx=="on":
		led.on()
	else:
		led.off()
	

def on_disconnect(client,userdata,rc):
	print "Disconnected..rc=%d" %(rc)
	

class worker(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.cmd_table = db("cmd_tb.db")
		self.fb_table = db("fb_tb.db")

	def con_to_broker(self):
		client.on_connect 	= on_connect
		client.on_message 	= on_message
		client.on_disconnect = on_disconnect
		client.connect("192.168.1.4",1883,60)

		client.loop_start()


	def run(self):

		self.con_to_broker()

		while True:
			dev_stat=led.read()
			client.publish("wa/thread1/publish",dev_stat,1)		# Echo to node2
			time.sleep(1)


	


def main():
	workerthread=worker()
	workerthread.start()

if __name__ == '__main__':
	main()
