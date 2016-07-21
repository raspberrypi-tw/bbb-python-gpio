#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# people_alarm_system.py
# Sense human and blink LED with PIR(Passive InfraRed Sensor) sensor
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.GPIO as GPIO
import time
 
WAIT_TIME = 200
GPIO.setup("P9_12", GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup("P9_15", GPIO.OUT)

def mycallback(channel):
    print "Motion detected @", time.ctime()
    blink_led()

def blink_led():
    for i in xrange(3) :
        GPIO.output("P9_15", GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output("P9_15", GPIO.LOW)
        time.sleep(0.5)

try:
    GPIO.add_event_detect("P9_12", GPIO.RISING, callback=mycallback, bouncetime=WAIT_TIME)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()                              

