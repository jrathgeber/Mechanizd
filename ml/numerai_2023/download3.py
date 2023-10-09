import numerapi
# some API calls do not require logging in
napi = numerapi.NumerAPI(verbosity="info")

# download current dataset => also check `https://numer.ai/data/v4`
napi.download_dataset("v4/train.parquet", "train.parquet")

# get current leaderboard
leaderboard = napi.get_leaderboard()

# check if a new round has started
if napi.check_new_round():
    print("new round has started within the last 12hours!")
else:
    print("no new round within the last 12 hours")

# provide api tokens
example_public_id = "somepublicid"
example_secret_key = "somesecretkey"
napi = numerapi.NumerAPI(example_public_id, example_secret_key)

# upload predictions
model_id = napi.get_models()['uuazed']
napi.upload_predictions("preds.csv", model_id=model_id)
# increase your stake by 1.2 NMR
napi.stake_increase(1.2)

# convert results to a pandas dataframe
import pandas as pd
df = pd.DataFrame(napi.daily_user_performances("uuazed"))