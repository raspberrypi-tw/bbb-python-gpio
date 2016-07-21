#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# push_button_poll.py
# Response when push button is pressed with poll way
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_12", GPIO.IN)

try:
    while True:
        if GPIO.input("P9_12") == GPIO.LOW:
            print("Button pressed @"), time.ctime()

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
