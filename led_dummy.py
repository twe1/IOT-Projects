ledpin=7
ip=11

cur_status = "off"


def on():
	global cur_status
	cur_status = "on"

def off():
	global cur_status
	cur_status = "off"

def read():
	global cur_status
	return cur_status

