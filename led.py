import RPi.GPIO as g 
def led_init():
	g.setwarnings(False)
	g.setmode(g.BOARD)
	g.setup(7,g.OUT)
def on():
	g.output(7,True)
def off():
	g.output(7,False)

led_init()