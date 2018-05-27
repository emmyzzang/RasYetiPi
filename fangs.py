#!/usr/bin/env python

import scrollphathd as sphd
from scrollphathd.fonts import font5x7

import time

sphd.rotate(180)

# Left Fang
sphd.set_pixel(2, 0, 0.5)
sphd.set_pixel(6, 0, 0.5)
sphd.set_pixel(3, 1, 0.5)
sphd.set_pixel(5, 1, 0.5)
sphd.set_pixel(4, 2, 0.5)

# Right Fang
sphd.set_pixel(11, 0, 0.5)
sphd.set_pixel(15, 0, 0.5)
sphd.set_pixel(12, 1, 0.5)
sphd.set_pixel(14, 1, 0.5)
sphd.set_pixel(13, 2, 0.5)
sphd.show()

time.sleep(5)

sphd.clear()

while True:

    sphd.write_string("Hello World! I am Yeti!!!! Rawrrr!!                ", x=0, y=0, font=font5x7, brightness=0.5)

    sphd.show()
    sphd.scroll()

    time.sleep(0.05)

"yeti-fang.py" 36L, 644C
