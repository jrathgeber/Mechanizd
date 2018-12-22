# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:33:01 2018

@author: Jason
"""

import tsfresh

from tsfresh.examples.robot_execution_failures import download_robot_execution_failures, \
    load_robot_execution_failures
download_robot_execution_failures()
timeseries, y = load_robot_execution_failures()