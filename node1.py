import paho.mqtt.client as mqtt
import time
def on_connect(client,userdata,rc):
	print "Connected to broker.." +str(rc)
	client.subscribe("wa/kitchen")

def on_message(client, userdata, msg):
	print "topic:",msg.topic," message:", str(msg.payload)
def on_disconnect(client,userdata, rc):
	print "Disconnect:", +str(rc)
client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.on_disconnect=on_disconnect
client.connect("test.mosquitto.org",1883,60)
client.loop_forever()
