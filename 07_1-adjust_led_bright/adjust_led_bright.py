#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# adjust_led_bright.py
# Adjust the bright of a led by software PWM
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.PWM as PWM
import time

PWM.start("P9_14", 0)

try:
    while True:
        duty_s = raw_input("Enter Brightness (0 to 100):")
        duty = int(duty_s)

        if duty >= 0 and duty <=100 :
	        PWM.set_duty_cycle("P9_14", duty)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    PWM.stop("P9_14")
    PWM.cleanup()
