#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# push_button_debounce.py
# Response when push button is pressed with poll way, and de-bounce by 
# software
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_12", GPIO.IN)

WAIT_TIME = 0.2
previousTime = time.time()

try:
    while True:
        currentTime = time.time()
        if GPIO.input("P9_12") == GPIO.LOW and (currentTime - previousTime) > WAIT_TIME:
            previousTime = currentTime
            print("Button pressed @"), time.ctime()

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
