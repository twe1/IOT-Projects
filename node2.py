import paho.mqtt.client as mqtt

def on_publish(client,userdata, mid):
	print "Data sent!"
def on_disconnect(client,userdata, rc):
	print "Disconnect: ",
	print rc
	mqttc.reconnect()

mqttc=mqtt.Client("python_pub")
mqttc.on_publish=on_publish
mqttc.on_disconnect=on_disconnect
mqttc.connect("test.mosquitto.org",1883)

print "Connected to broker.."

while True:
	msg=raw_input("Enter the message: ")
	mqttc.publish("wa/kitchen", msg,1)
	mqttc.loop()