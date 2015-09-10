import threading
import paho.mqtt.client as mqtt

class sub(threading.Thread):
	def __init__(self,client):
		threading.Thread.__init__(self)
		self.client = client
	
	def run(self):
		self.client.loop_forever()

def on_connect(client,userdata,rc):
	print "Connected to broker. rc=%s" %(str(rc))
	client.subscribe("wa/topic1")

def on_message(client,userdata,msg):
	print "Topic: %s, Message: %s" %(msg.topic,msg.payload)

def main():
	client=mqtt.Client("wirewords2")
	client.on_connect=on_connect
	client.on_message=on_message
	client.connect("test.mosquitto.org",1883,60)

	sub_thread=sub(client)
	sub_thread.start()

if __name__ == '__main__':
	main()

