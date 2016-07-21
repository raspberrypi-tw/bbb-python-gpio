#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# hc_sr04_measure_distance.py
# Measure the distance between HC-SR04 and nearest wall or solid object.
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_12", GPIO.OUT, initial=GPIO.LOW)         # TRIGGER_PIN
GPIO.setup("P9_15", GPIO.IN,  pull_up_down=GPIO.PUD_UP) # ECHO_PIN

v = 343		# (331 + 0.6*20)

def measure() :
    GPIO.output("P9_12", GPIO.HIGH)
    time.sleep(0.00001)	# 10uS 
    GPIO.output("P9_12", GPIO.LOW)
    pulse_start = time.time()

    while GPIO.input("P9_15") == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input("P9_15") == GPIO.HIGH:
        pulse_end = time.time()

    t = pulse_end - pulse_start

    d = t * v
    d = d/2

    return d*100


def measure_average() :
    d1 = measure()
    time.sleep(0.05)
    d2 = measure()
    time.sleep(0.05)
    d3 = measure()
    distance = (d1 + d2 + d3) / 3
	
    return distance

try :
    while True:
        distance = measure_average()
        print "Distance : %.1f" % distance
        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
