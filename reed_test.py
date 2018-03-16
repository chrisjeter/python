import time
import RPi.GPIO as io

def monitor_door():
	io.setmode(io.BCM)
	pir_pin = 18
	door_pin = 23
 	io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp
 	while True:
		if io.input(door_pin):
			print("DOOR ALARM!")
    		time.sleep(0.5)


monitor_door()
