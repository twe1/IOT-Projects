import paho.mqtt.client as mqtt
import led

client=mqtt.Client()  # Global declaration

def on_connect(client,userdata,rc):
	print "\nNode Connected to broker. rc=%d\n\n" %(rc)
	client.subscribe("wa/thread2/publish")

def on_message(client,userdata,msg):
	if msg.payload == "on":
		led.on()
	else:
		led.off()

	dev_stat = led.read()

	print "\t%s" %(dev_stat)
	client.publish("wa/thread1/publish",dev_stat,1)		# Echo to node2

def on_disconnect(client,userdata,rc):
	print "Disconnected..rc=%d" %(rc)
	
def node():
	client.on_connect 	= on_connect
	client.on_message 	= on_message
	client.on_disconnect = on_disconnect
	client.connect("192.168.1.4",1883,60)

	client.loop_start()
	
	try:
		while True:
			pass
	except KeyboardInterrupt as e:
		print e
		client.loop_stop()	
		client.disconnect()
	

if __name__ == '__main__':
	node()	