import paho.mqtt.client as mqtt
import time

def on_connect(client,userdata,rc):
	client.subscribe("wa/kitchen2")

def on_message(client, userdata, msg):
	print "Topic:",msg.topic," Message from node2:", str(msg.payload)

def on_publish(client,userdata, mid):
	print "Data sent!"

def on_disconnect(client,userdata, rc):
	print "Disconnect:",
	print rc
	client.reconnect()

client=mqtt.Client("wirewords2")
client.on_connect=on_connect
client.on_message=on_message
client.on_publish=on_publish
client.on_disconnect=on_disconnect
client.connect("test.mosquitto.org",1883,60)

print "Connected to broker.."

while True:
	mesg=raw_input("Enter the message: ")
	client.publish("wa/kitchen", mesg,1)
	client.loop()
