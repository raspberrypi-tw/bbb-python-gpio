#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# photoresistor.py
# Sense the light by photoresistor
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.ADC as ADC
import time
 
ADC.setup()

try:
    while True:
        r = ADC.read("P9_40")
        vr = r * 1.8 #1.8V

        print vr
        time.sleep(1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    pass

