import RPi.GPIO as g 
ledpin=7
ip=11

def led_init():
	g.setwarnings(False)
	g.setmode(g.BOARD)
	g.setup(ledpin,g.OUT)
	g.setup(ip, g.IN)
def on():
	g.output(ledpin,True)
def off():
	g.output(ledpin,False)
def read():
	value=g.input(ip)
	return value

led_init()