# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 06:52:28 2017

@author: Jason
"""

from subprocess import Popen
import time

#Start IB Gateway
ib = [r"F:\\GitHub\\ib-controller\\resources\\IBControllerGatewayStart.bat"]
ib_prog = Popen(ib)

time.sleep(10)

#mt1 = [r"C:\\Program Files (x86)\\FOREX.com US\\terminal.exe"]
#mt1_prog = Popen(mt1)
#time.sleep(10)

mt2 = [r"C:\\Program Files (x86)\\FOREX.com US2\\terminal.exe"]
mt2_prog = Popen(mt2)

time.sleep(10)

mt3 = [r"C:\\Program Files (x86)\\FOREX.com US3\\terminal.exe"]
mt3_prog = Popen(mt3)

time.sleep(10)

#z1 = [r"F:\\Zorro\\Gain_174\\Zorro.exe", "-trade", "Z1", "-c" , "R1"]
#z1_prog = Popen(z1)
#time.sleep(10)

z2 = [r"F:\\Zorro\\Gain_174\\Zorro.exe", "-trade", "Z2", "-c" , "R2"]
z1_prog = Popen(z2)

time.sleep(10)

z12 = [r"F:\\Zorro\\Gain_174\\Zorro.exe", "-trade", "Z12", "-c" , "R3"]
z12_prog = Popen(z12)

time.sleep(10)

j12 = [r"F:\\Zorro\\Gain_174\\Zorro.exe", "-trade", "J12", "-c" , "J1"]
j12_prog = Popen(j12)

