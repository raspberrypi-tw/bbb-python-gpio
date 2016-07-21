#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# tilt_switch.py
# Response when tilt switch is triggered with interrupt way, and 
# de-bounces by software
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.GPIO as GPIO
import time
 
WAIT_TIME = 200
GPIO.setup("P9_12", GPIO.IN, pull_up_down=GPIO.PUD_UP)

def mycallback(channel):                                                 
    print("Switch tilted @"), time.ctime()

try:
    GPIO.add_event_detect("P9_12", GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
