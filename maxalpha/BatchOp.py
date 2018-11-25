# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 21:41:28 2018

@author: Jason
"""

# -*- coding: utf-8 -*-

import os;
import RightEdge as RE;
import Maxalpha2 as MA;
import Optimise as OP;
import time;
import SymbolConfig as SC;


os.chdir('C:\dep\\maxalpha\\')

daterun = time.strftime("%Y%m%d")

print(daterun)


OP.optimise('MaxAlpha')