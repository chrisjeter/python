#!/usr/bin/python
import time, requests, logging, RPi.GPIO as io, Adafruit_DHT as dht, httplib, urllib
from multiprocessing import Process

io.setmode(io.BCM)
pir_pin = 18
door_pin = 23
io.setup(door_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp
door = ""
still_open = ""
temperature = ""
humidity = ""


def alert(door_state):
    request_url = "https://api.mailgun.net/v3/mg.kansashunter.org/messages"
    api_key = "key-e7a8070aaf3649a7494f8333edf04e1b"
    fromaddr = "Safe Monitor  <SafeMonitor@kansashunter.org>"
    toaddr = ["cjeter+mailgun@gmail.com", "7856919005@txt.att.net"]
    open_body = "The door to the safe has been OPENED!"
    still_open_body = "The door to the safe has been OPENED \
                       for longer than the TIMEOUT!"
    logging.captureWarnings(True)
    if (door_state == "open"):
        return requests.post(
        request_url,
        auth=("api", api_key),
        data={"from": fromaddr,
              "to": toaddr,
              "subject": "SAFE ALART",
              "text": open_body})
    elif (door_state == "still_open"):
        return requests.post(
        request_url,
        auth=("api", api_key),
        data={"from": fromaddr,
              "to": toaddr,
              "subject": "SAFE ALART",
              "text": still_open_body})

#def update_thing():
#    thing_url = "https://api.thingspeak.com"
#    thing_api_key = "WXM1DA1C87VPHTIZ"
#    return requests.post(
#    thing_url,

def update_thing():
    global temperature
    global humidity
    #params = urllib.urlencode({'field1': temperature, 'key' : 'WXM1DA1C87VPHTIZ'})
    params = urllib.urlencode({'field1': temperature, 'field2' : humidity, 'key' : 'WXM1DA1C87VPHTIZ'})
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPSConnection("api.thingspeak.com:443")
    #try:
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print temperature, humidity
    print response.status, response.reason
    data = response.read()
    conn.close()
    #except:
    #    print "connection failed"

def door_is_open():
    global still_open
    open_for = time.time() +5
    while (io.input(door_pin) == 1):
        if time.time() > open_for:
         #alert("still_open")
            print "alert_still_open"
            still_open = "yes"
            break
        else:
            time.sleep(1)
            print "Door still open"
    door = "closed"

def monitor_door():
    global still_open
    global door
    while True:
        if io.input(door_pin) == 0:
            door = "closed"
            still_open = ""
            time.sleep(.01)
        elif io.input(door_pin) == 1:
            door = "open"
            if door == "open":
                if still_open == "yes":
                    door_is_open()
                elif still_open == "":
                    print "open"
                    door_is_open()
        time.sleep(.1)

def monitor_temp():
    global temperature
    global humidity
    high_temp = 32
    high_humidity = 30
    dht_pin = 4
    while True:
        humidity, raw_temp = dht.read_retry(dht.DHT22, dht_pin)
        #temperature = 9.0/5.0 * raw_temp +32
        temperature = round( 9.0/5.0 * raw_temp +32, 1)
        if humidity is not None and raw_temp is not None:
            print 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity)
            update_thing()
        else:
            print 'Failed to get reading. Try again!'
        time.sleep(300)

if __name__ == '__main__':
    p1 = Process(target=monitor_temp)
    p2 = Process(target=monitor_door)
    p1.start()
    p2.start()

