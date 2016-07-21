#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+
#|R|i|c|e|L|e|e|.|c|o|m|
#+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, ricelee.com
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# joystick_mapping_keyboard.py
# Mapping keyboard Up/Down/Right/Left by joystick 
#
# Author : sosorry
# Date   : 05/01/2016

import Adafruit_BBIO.ADC as ADC
import time
from evdev import UInput, ecodes as e
 
ADC.setup()
ui = UInput()

try:
    while True:
        x = ADC.read("P9_40")
        y = ADC.read("P9_38")
        vx = x * 1.8 #1.8V
        vy = y * 1.8 #1.8V

        print "--------------------------------------------"  
        print("X : {}  Y : {} ".format(vx, vy))

        # LEFT
        if vx > 1.6 :
            ui.write(e.EV_KEY, e.KEY_LEFT,  1)  
            ui.write(e.EV_KEY, e.KEY_RIGHT, 0)
            ui.syn()
        # RIGHT
        elif vy < 0.1 :
            ui.write(e.EV_KEY, e.KEY_RIGHT, 1)
            ui.write(e.EV_KEY, e.KEY_LEFT,  0)
            ui.syn()
        else :
            ui.write(e.EV_KEY, e.KEY_RIGHT, 0)
            ui.write(e.EV_KEY, e.KEY_LEFT,  0)
            ui.syn()

        # DOWN
        if vx > 1.6 :
            ui.write(e.EV_KEY, e.KEY_DOWN,  1)  
            ui.write(e.EV_KEY, e.KEY_UP,    0)
            ui.syn()
        # UP
        elif vx < 0.1 :
            ui.write(e.EV_KEY, e.KEY_DOWN, 0)
            ui.write(e.EV_KEY, e.KEY_UP,   1)
            ui.syn()
        else :
            ui.write(e.EV_KEY, e.KEY_DOWN, 0)
            ui.write(e.EV_KEY, e.KEY_UP,   0)
            ui.syn()

        time.sleep(0.1)

except KeyboardInterrupt:
    print "Exception: KeyboardInterrupt"

finally:
    pass

