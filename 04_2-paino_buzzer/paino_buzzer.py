#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# paino_buzzer.py
# Make the buzzer sound like a piano
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.GPIO as GPIO
import time
 
GPIO.setup("P9_11", GPIO.OUT)   # Buzzer
GPIO.setup("P9_12", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_13", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_14", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_15", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_16", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_23", GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup("P9_27", GPIO.IN, pull_up_down=GPIO.PUD_UP)

MELODY_DO = 523
MELODY_RE = 587
MELODY_ME = 659
MELODY_FA = 698
MELODY_SO = 784
MELODY_LA = 880
MELODY_SI = 988

WAIT_TIME = 200
DURATION = 0.2

def buzz(pitch) :
    period = 1.0 / pitch
    half_period = period / 2
    cycles = int(DURATION * pitch)

    for i in xrange(cycles) :
        GPIO.output("P9_11", GPIO.HIGH)
        time.sleep(half_period)
        GPIO.output("P9_11", GPIO.LOW)
        time.sleep(half_period)

def mycallback(channel):
    print("Button pressed @:"), channel, time.ctime()

    if channel == "P9_12":
        buzz(MELODY_DO)
    elif channel == "P9_13":
        buzz(MELODY_RE)
    elif channel == "P9_14":
        buzz(MELODY_ME)
    elif channel == "P9_15":
        buzz(MELODY_FA)
    elif channel == "P9_16":
        buzz(MELODY_SO)
    elif channel == "P9_23":
        buzz(MELODY_LA)
    elif channel == "P9_27":
        buzz(MELODY_SI)

try:
    GPIO.add_event_detect("P9_12", GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)
    GPIO.add_event_detect("P9_13", GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)
    GPIO.add_event_detect("P9_14", GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)
    GPIO.add_event_detect("P9_15", GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)
    GPIO.add_event_detect("P9_16", GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)
    GPIO.add_event_detect("P9_23", GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)
    GPIO.add_event_detect("P9_27", GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    GPIO.cleanup()          
