#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# led_on.py
# Turn on a led 
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_12", GPIO.OUT)

print("LED is on")
GPIO.output("P9_12", GPIO.HIGH)    
time.sleep(3)

GPIO.cleanup()   

