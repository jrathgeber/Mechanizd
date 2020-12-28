# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 17:02:52 2020

@author: Jason
"""

from numerapi import NumerAPI

from numerox.numerai import status_block
from numerox.numerai import upload_status

import time


def upload(filename,
           tournament,
           public_id,
           secret_key,
           block=True,
           n_tries=100,
           sleep_seconds=60,
           verbose=False,
           model_id=None):
    """
    Upload tournament submission (csv file) to Numerai.

    Accounts with multiple models must specify model_id

    If upload fails then retry upload `n_tries` times, pausing `sleep_seconds`
    between each try.

    If block is True (default) then the scope of your token must be both
    upload_submission and read_submission_info. If block is False then only
    upload_submission is needed.

    """
    #tournament = nx.tournament_int(tournament)
    tournament = 8
    
    count = 0
    napi = NumerAPI(public_id=public_id,
                    secret_key=secret_key,
                    verbosity='warning')
    models = napi.get_models()
    if len(models) > 1 and model_id is None:
        raise Exception(
            f"Account has multiple models - you must specify model_id from {models}"
        )
    elif model_id and model_id not in models.values():
        raise Exception(
            f"Specified model_id {model_id} not found in account models {models}"
        )

    while count < n_tries:
        try:
            upload_id = napi.upload_predictions(filename, tournament=tournament, model_id=model_id)
            
            if block:
                status = status_block(upload_id, public_id, secret_key, model_id=model_id)
            else:
                status = upload_status(upload_id, public_id, secret_key, model_id=model_id)
            break

        except Exception as e:  # noqa
            if str(e).startswith("Can't update submission after deadline"):
                # Bailout with error message and do not retry uploads
                raise Exception(e)
            else:
                print('Upload exception - %s' % e)
                time.sleep(sleep_seconds)
        count += 1

    else:
        raise Exception('Upload failed after reaching max retries')

    return upload_id, status