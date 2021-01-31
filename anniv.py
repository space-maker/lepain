# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("joyeux anniversaire sale moche")

import platform
import PIL.Image
import os
chemin = os.path.dirname( __file__)+"/doge.jpg"
chemin = chemin.replace("\\", "/")
doge=PIL.Image.open(chemin)
doge.show()
try:
    import winsound
    beep = winsound.Beep
except ImportError:
    def beep(f, d):
        s = 8000
        hp = int(s/f/2)
        b = chr(255)*hp+chr(0)*hp
        b *= int(d*f)
        a = file('/dev/audio', 'wb')
        a.write(b)
        a.close()

c = [
    (784, 300),
    (784, 300),
    (880, 400),
    (784, 300),
    (1047, 350),
    (988, 600),
    (784, 300),
    (784, 300),
    (880, 400),
    (784, 300),
    (1175, 350),
    (1047, 600),
    (784, 300),
    (784, 300),
    (1568, 350),
    (1319, 300),
    (1047, 350),
    (988, 600),
    (1397, 300),
    (1397, 300),
    (1319, 350),
    (1047, 300),
    (1175, 300),
    (1047, 500),
]

s = c + c

for f, d in s:
    beep(f, d)
