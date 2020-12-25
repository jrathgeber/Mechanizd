# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:36:43 2020

@author: Jason
"""

# tutorial/01-create-workspace.py
from azureml.core import Workspace

ws = Workspace.create(name='numerai_test', # provide a name for your workspace
                      subscription_id='aa180ff5-91a3-4047-81d8-9f717e5afb7f', # provide your subscription ID
                      resource_group='numerai', # provide a resource group name
                      create_resource_group=True,
                      location='eastus2') # For example: 'westeurope' or 'eastus2' or 'westus2' or 'southeastasia'.

# write out the workspace details to a configuration file: .azureml/config.json
ws.write_config(path='.azureml')