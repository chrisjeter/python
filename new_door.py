#!/usr/bin/python
import time
import smtplib
import RPi.GPIO as io
io.setmode(io.BCM)
pir_pin = 18
door_pin = 23
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp

def door_is_open():
    global door_open
    open_for = time.time() +30
    while (io.input(door_pin) == 1):
        if time.time() > open_for:
            alert_still_open()
            print "The timeout of %s was reached." % open_for
            break
        else:
			print "Door still open"
			time.sleep(20)
    else:
		door_open = 0
		print "Door Closed again"



door_is_open()
