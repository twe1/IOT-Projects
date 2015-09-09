import paho.mqtt.client as mqtt

def on_publish(client,userdata, mid):
	print "data sent"
def on_disconnect(client,userdata, rc):
	print "Disconnect: ",
	print rc
	mqttc.connect("test.mosquitto.org",1883)
	
mqttc=mqtt.Client("python_pub")
mqttc.on_publish=on_publish
mqttc.on_disconnect=on_disconnect
mqttc.connect("test.mosquitto.org",1883)

print "connected to broker"

while True:
	msg=raw_input("Enter the message: ")
	mqttc.publish("wa/kitchen", msg,1)
	mqttc.loop()