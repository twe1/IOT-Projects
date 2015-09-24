
import paho.mqtt.client as mqtt
import threading 

import time
from database import db

try:
	import led
except Exception, e:
	import led_dummy as led
	print e


client=mqtt.Client()  # Global declaration
db_obj=db()
stopThread = threading.Event()

#broker = "192.168.1.4"
broker = "test.mosquitto.org"

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
		client.connect(broker,1883,60)

		client.loop_start()


	def run(self):

		self.con_to_broker()

		while not stopThread.isSet():
			dev_stat=led.read()
			client.publish("wa/thread1/publish",dev_stat,1)		# Echo to node2
			time.sleep(1)

	def join(self,timeout = None):
		client.loop_stop()	
		client.disconnect()
		threading.Thread.join(self,timeout)
		print "\n\t\tKilled thread !!"
	


def main():
	workerthread=worker()
	workerthread.start()

	try:
		while True:
			pass
	except KeyboardInterrupt as e:
		print e
		stopThread.set()
		workerthread.join()

		

if __name__ == '__main__':
	main()
