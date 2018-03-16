#!/usr/bin/python
import time
timeout = time.time() +.05
count = 1
while count < 1000:
	if time.time() > timeout:
		print "The timeout of %s was reached." % timeout
		break
	print count, " is  less than 5"
   	count = count + 1
else:
   print count, "WE BEAT THE TIMEOUT"
