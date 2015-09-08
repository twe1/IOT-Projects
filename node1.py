import paho.mqtt.client as mqtt
def on_connect(client,userdata,rc):
	print "connected to broker " +str(rc)
	client.subscribe("wa/kitchen")

def on_message(client, userdata, msg):
	print "topic:",msg.topic," message:", str(msg.payload)

client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("test.mosquitto.org",1883,60)
client.loop_forever()