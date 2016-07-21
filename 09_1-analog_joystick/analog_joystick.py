#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# analog_joystick.py
# Read analogue joystick from AINx pin
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.ADC as ADC
import time
 
ADC.setup()

try:
    while True:
        x = ADC.read("P9_40")
        y = ADC.read("P9_38")
        vx = x * 1.8 #1.8V
        vy = y * 1.8 #1.8V

        print vx, vy
        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    pass


