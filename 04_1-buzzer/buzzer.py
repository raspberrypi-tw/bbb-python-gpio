#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# buzzer.py
# Make the buzzer to sound with interactive way
#
# Author : Raspberry Pi Cookbook

import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_12", GPIO.OUT)

def buzz(pitch, duration) :
    period = 1.0 / pitch
    half_period = period / 2
    cycles = int(duration * pitch)
    for i in xrange(cycles) :
        GPIO.output("P9_12", GPIO.HIGH)
        time.sleep(half_period)
        GPIO.output("P9_12", GPIO.LOW)
        time.sleep(half_period)

try:
    while True :
        pitch_s = raw_input("Enter Pitch (200 to 2000): ")
        duration_s = raw_input("Enter Duration (seconde): ")
        buzz(float(pitch_s), float(duration_s))

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
