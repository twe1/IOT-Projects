import threading 
import paho.mqtt.client as mqtt 

class pub(threading.Thread):
	
	def __init__(self,client):
		print "In cnstr"
		threading.Thread.__init__(self)
		self.client = client
		self.client.loop()


	def run(self):
		while True:
			msg=raw_input("Enter msg: ")
			self.client.publish("wa/topic1",msg,1)
			self.client.loop()
		
	
def on_connect(client,userdata,rc):
	print "Connected to broker..rc=%s" %(str(rc))
	

def on_disconnect(client,userdata,rc):
	print "Disconnected..rc=%s" %(str(rc))
	client.reconnect()

def main():
	client=mqtt.Client("wirewords1")
	client.on_connect= on_connect
	client.on_disconnect= on_disconnect
	client.connect("test.mosquitto.org", 1883,60)


	pub_thread=pub(client)
	pub_thread.start()


if __name__ == '__main__':
	main()









