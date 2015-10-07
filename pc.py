import paho.mqtt.client as mqtt
from database import db
import time

while True:
	try:
		db_sw = db("sw")
		db_light = db("light")
		break
	except Exception as e:
		print e
	time.sleep(0.5)

prev_light_status = db_light.fetch()
broker = "192.168.1.4"
#broker = "test.mosquitto.org"

try:
	print "\t%s" %(prev_light_status)
except Exception, e:
	print e

def on_connect(client,userdata,rc):
	print "\nNode Connected to broker. rc=%d\n\n" %(rc)
	client.subscribe("wa/thread1/publish")

def on_message(client,userdata,msg):
	global prev_light_status
	
	cur_light_status = msg.payload

	if prev_light_status!= cur_light_status :
		print "\t%s" %(cur_light_status)
		db_light.insert(cur_light_status)
		prev_light_status = cur_light_status

def on_disconnect(client,userdata,rc):
	print "Disconnected..rc=%d" %(rc)
	
def node():
	global prev_sw_status

	client=mqtt.Client()
	
	client.on_connect 	= on_connect
	client.on_message 	= on_message
	client.on_disconnect = on_disconnect
	client.connect(broker,1883,60)

	client.loop_start()
	
	try:
		while True:
			cur_sw_status = db_sw.fetch()
			time.sleep(0.5)
			if prev_light_status != cur_sw_status:
				client.publish("wa/thread2/publish",cur_sw_status, 1)
				print cur_sw_status
			

			

	except KeyboardInterrupt as e:
		print e
		client.loop_stop()	
		client.disconnect()
	

if __name__ == '__main__':
	node()	