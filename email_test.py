#!/usr/bin/python

import smtplib

sender = 'cjeter@outcast.homeunix.org'
receivers = ['cjeter+pi@gmail.com']

message = """From: SAFE DOOR <cjeter@outcast.homeunix.org>
To: To Person <cjeter+pi@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('192.168.2.3')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"
