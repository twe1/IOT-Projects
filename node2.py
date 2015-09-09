import paho.mqtt.client as mqtt

def on_connect(client,userdata,rc):
	client.subscribe("wa/kitchen")

def on_message(client, userdata, mesg):
	print "Topic:",mesg.topic," Messagefrom node1:", str(mesg.payload)

def on_publish(client,userdata, mid):
	print "Data sent!"

def on_disconnect(client,userdata, rc):
	print "Disconnect: ",
	print rc
	mqttc.reconnect()

mqttc=mqtt.Client("wirewords")
mqttc.on_publish=on_publish
mqttc.on_disconnect=on_disconnect
mqttc.on_connect=on_connect
mqttc.on_message=on_message
mqttc.connect("test.mosquitto.org",1883,60)

print "Connected to broker.."

while True:
	msg=raw_input("Enter the message: ")
	mqttc.publish("wa/kitchen2", msg,1)
	mqttc.loop()