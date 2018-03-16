#!/usr/bin/python
import Adafruit_DHT as dht

high_temp = 32
high_humidity = 30
dht_pin = 4
humidity, raw_temp = dht.read_retry(dht.DHT22, dht_pin)
temperature = 9.0/5.0 * raw_temp +32

if humidity is not None and raw_temp is not None:
    print 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity)
else:
    print 'Failed to get reading. Try again!'

if humidity > high_humidity:
    print "Humidity to HIGH!"
if temperature > high_temp:
    print "Temp is TO HIGH!"

