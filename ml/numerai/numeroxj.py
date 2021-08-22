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
            if str(e).startswith("Can't update submission after deadline") or str(e).startswith("Cannot query field"):
                # Bailout with error message and do not retry uploads
                raise Exception(e)
            else:
                print('Upload exception - %s' % e)
                time.sleep(sleep_seconds)
        count += 1

    else:
        raise Exception('Upload failed after reaching max retries')

    return upload_id, status



def sstatus_block(upload_id, public_id, secret_key, verbose=False, model_id=None):
    """
    Block until status completes; then return status dictionary.

    The scope of your token must must include read_submission_info.
    """
    t0 = time.time()
    if verbose:
        print("metric                  value   minutes")
    seen = []
    fmt_f = "{:<19} {:>9.4f}   {:<.4f}"
    fmt_b = "{:<19} {:>9}   {:<.4f}"
    n_tries = 3
    count = 0
    while count < n_tries:
        count += 1
        status = upload_status(upload_id, public_id, secret_key, model_id=model_id)
        t = time.time()
        for key, value in status.items():
            if value is not None and key not in seen:
                seen.append(key)
                if key == 'filename':
                    continue
                minutes = (t - t0) / 60
                if verbose:
                    #if key in ('originality'):
                    #if key in ('originality', 'concordance'):
                    print(fmt_b.format(key, str(value), minutes))
                    #else:
                    print(fmt_f.format(key, value, minutes))
        if len(status) == len(seen):
            break
        seconds = min(5 + int((t - t0) / 100.0), 30)
        time.sleep(seconds)
    if verbose:
        t = time.time()
        minutes = (t - t0) / 60
        iss = is_stakeable(status)
        print(fmt_b.format('stakeable', str(iss), minutes))
    return status


def is_stakeable(status):
    "Is sumission stakeable? Pending status returns False."
    #if None in status.values():
    #    return False
    #iss = status['consistency'] >= 100 * CONSISTENCY_GTE
    #iss = iss and status['concordance']
    #return iss
    return False


def xx_upload_status(upload_id, public_id, secret_key, model_id=None):
    "Dictionary containing the status of upload"
    napi = NumerAPI(public_id=public_id,
                    secret_key=secret_key,
                    verbosity='warning')
    status_raw = napi.submission_status(model_id=model_id)
    status = {}
    for key, value in status_raw.items():
        if isinstance(value, dict):
            value = value['value']
        status[key] = value
    return status
