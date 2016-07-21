#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# pwm_led.py
# Make led to be bright and to be dark by software PWM
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.PWM as PWM
import time

PWM.start("P9_14", 0)

try:
    while True:
        for dc in xrange(0, 101, 5): 
            PWM.set_duty_cycle("P9_14", dc)
            time.sleep(0.1)
        time.sleep(0.5)

        for dc in xrange(100, -1, -5):
            PWM.set_duty_cycle("P9_14", dc)
            time.sleep(0.1)
        time.sleep(0.5)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    PWM.stop("P9_14")
    PWM.cleanup()


