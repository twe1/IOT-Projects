import paho.mqtt.client as mqtt
from database import db

db_sw = db("sw")
db_light = db("light")
prev_status= db_light.fetch() 

broker = "192.168.1.4"
#broker = "test.mosquitto.org"

print "\t%s" %(prev_status)


def on_connect(client,userdata,rc):
	print "\nNode Connected to broker. rc=%d\n\n" %(rc)
	client.subscribe("wa/thread1/publish")

def on_message(client,userdata,msg):
	global prev_status
	
	cur_status = msg.payload

	if prev_status!= cur_status :
		print "\t%s" %(cur_status)
		db_light.insert(cur_status)
		prev_status = cur_status

def on_disconnect(client,userdata,rc):
	print "Disconnected..rc=%d" %(rc)
	
def node():
	client=mqtt.Client()
	
	client.on_connect 	= on_connect
	client.on_message 	= on_message
	client.on_disconnect = on_disconnect
	client.connect(broker,1883,60)

	client.loop_start()
	
	try:
		while True:
			cur_cmd = raw_input()		# Link with Webapp here
			prev_status = db_light.fetch()
			
			if prev_status != cur_cmd:
				client.publish("wa/thread2/publish",cur_cmd, 1)
				db_sw.insert(cur_cmd)

	except KeyboardInterrupt as e:
		print e
		client.loop_stop()	
		client.disconnect()
	

if __name__ == '__main__':
	node()	