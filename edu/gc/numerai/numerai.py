# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:59:51 2020

@author: Jason
"""

# [START setup]
import datetime
import os
import subprocess

from sklearn.preprocessing import LabelEncoder
import pandas as pd
from google.cloud import storage
import xgboost as xgb


# TODO: REPLACE 'BUCKET_CREATED_ABOVE' with your GCS BUCKET_ID
BUCKET_ID = 'jason_general_data'
# [END setup]

# ---------------------------------------
# 1. Add code to download the data from GCS (in this case, using the publicly hosted data).
# AI Platform will then be able to use the data when training your model.
# ---------------------------------------
# [START download-data]
census_data_filename = 'numerai_training_data.csv'

# Public bucket holding the census data
bucket = storage.Client().bucket('jason_general_data')

# Path to the data inside the public bucket
#data_dir = 'ai-platform/census/data/'
data_dir = ''

# Download the data
blob = bucket.blob(''.join([data_dir, census_data_filename]))
blob.download_to_filename(census_data_filename)
# [END download-data]