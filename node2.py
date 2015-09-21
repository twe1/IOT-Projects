import paho.mqtt.client as mqtt

def on_connect(client,userdata,rc):
	print "\nNode Connected to broker. rc=%d\n\n" %(rc)
	client.subscribe("wa/thread1/publish")

def on_message(client,userdata,msg):
	print "\t%s" %(msg.payload)

def on_disconnect(client,userdata,rc):
	print "Disconnected..rc=%d" %(rc)
	
def node():
	client=mqtt.Client()
	
	client.on_connect 	= on_connect
	client.on_message 	= on_message
	client.on_disconnect = on_disconnect
	client.connect("192.168.1.4",1883,60)

	client.loop_start()
	
	try:
		while True:
			msg=raw_input()
			client.publish("wa/thread2/publish",msg, 1)
	except KeyboardInterrupt as e:
		print e
		client.loop_stop()	
		client.disconnect()
	

if __name__ == '__main__':
	node()	