# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 06:52:28 2017

@author: Jason
"""

from subprocess import Popen



models = ('downloadj','J12','J12a','J12b','J12c')

for model in models:

    j12 = [r"F:\\Zorro\\Zorro_19X\\Zorro.exe", "-run", model, "-c" , "J1"]
    j12_prog = Popen(j12)
   
    stdout, stderr = j12_prog.communicate()

