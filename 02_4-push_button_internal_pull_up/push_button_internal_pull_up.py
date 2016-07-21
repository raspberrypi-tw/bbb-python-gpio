#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# push_button_internal_pull_up
# Response when push button is pressed with interrupt way, and de-bounces 
# by software. The GPIO input uses the internal pull-up resistor(50k).
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_12", GPIO.IN, pull_up_down=GPIO.PUD_UP)
WAIT_TIME = 200

def mycallback(channel):                                                 
    print("Button pressed @"), time.ctime()

try:
    GPIO.add_event_detect("P9_12", GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)

    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
