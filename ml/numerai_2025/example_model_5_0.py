from numerapi import NumerAPI
import pandas as pd
import json

print("Starting up : connecting to NumerAI")

napi = NumerAPI()

# Download data
#napi.download_dataset("v4.2/train_int8.parquet");
#napi.download_dataset("v4.2/features.json");

def main(contest):

    #contest = str(504)
    directory = 'F:/Numerai/numerai' + contest + '/'
    dataset_name = "v5.0"

    print("Reading feature metadata")

    # Load data
    # feature_metadata = json.load(open("v4.2/features.json"))
    feature_metadata = json.load(open(f"{directory + dataset_name}/features.json"))

    features = feature_metadata["feature_sets"]["medium"] # use "all" for better performance. Requires more RAM.
    train = pd.read_parquet(f"{directory + dataset_name}/train_int8.parquet", columns=["era"]+features+["target"])

    # For better models, join train and validation data and train on all of it
    # napi.download_dataset("v4.2/validation_int8.parquet");
    # validation = pd.read_parquet("v4.2/validation_int8.parquet", columns=["era"]+features+["target"])
    # validation = validation[validation["data_type"] == "validation"] # drop rows which don't have targets yet
    # train = pd.concat([train, validation])

    print("Training the model I think ")

    # Downsample for speed
    train = train[train["era"].isin(train["era"].unique()[::4])]  # skip this step for better performance


    # Train model
    import lightgbm as lgb
    model = lgb.LGBMRegressor(
        n_estimators=2000,  # If you want to use a larger model we've found 20_000 trees to be better
        learning_rate=0.01, # and a learning rate of 0.001
        max_depth=5, # and max_depth=6
        num_leaves=2**5-1, # and num_leaves of 2**6-1
        colsample_bytree=0.1
    )
    model.fit(
        train[features],
        train["target"]
    );

    print("All Done !!")

    # Define predict function
    def predict(live_features: pd.DataFrame) -> pd.DataFrame:
        live_predictions = model.predict(live_features[features])
        submission = pd.Series(live_predictions, index=live_features.index)
        return submission.to_frame("prediction")

    # Pickle predict function
    import cloudpickle
    p = cloudpickle.dumps(predict)
    with open("predict_barebones.pkl", "wb") as f:
        f.write(p)

    # Download file if running in Google Colab
    #try:
    #    from google.colab import files
    #    files.download('predict_barebones.pkl')
    #except:
    #    pass

