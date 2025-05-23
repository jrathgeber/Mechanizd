from lightgbm import LGBMRegressor
import gc
import json
import pandas as pd
import numpy as np
from tqdm import tqdm

from numerapi import NumerAPI

from utils_old import (
    save_model,
    load_model,
    neutralize,
    validation_metrics,
    ERA_COL,
    DATA_TYPE_COL,
    TARGET_COL,
    EXAMPLE_PREDS_COL,
)


def main(contest):

    napi = NumerAPI()

    current_round = napi.get_current_round()

    #
    # Tournament data changes every week so we specify the round in their name. Training
    # and validation data only change periodically, so no need to download them every time.
    # print("Downloading dataset files...")

    contest = str(596)
    directory = 'F:/Numerai/numerai' + contest + '/'
    dataset_name = "v5.0"

    feature_set_name = "medium"

    # Path(f"./{dataset_name}").mkdir(parents=False, exist_ok=True)

    # we'll use the int8 in this example in order to save RAM.
    # if you remove the int8 suffix for each of these files, you'll get features between 0 and 1 as floats.
    # int_8 files are much smaller...
    # but are harder to work with because some packages don't like ints and the way NAs are encoded.

    # napi.download_dataset(f"{dataset_name}/train.parquet", f"{directory + dataset_name}/train.parquet")
    # napi.download_dataset(f"{dataset_name}/validation.parquet", f"{directory + dataset_name}/validation.parquet")
    # napi.download_dataset(f"{dataset_name}/live_int8.parquet", f"{directory + dataset_name}/live_int8_{current_round}.parquet")

    # napi.download_dataset(f"{dataset_name}/train_int8.parquet", f"{directory + dataset_name}/train_int8.parquet")
    # napi.download_dataset(f"{dataset_name}/validation_int8.parquet", f"{directory + dataset_name}/validation_int8.parquet")
    napi.download_dataset(
        f"{dataset_name}/live.parquet",
        f"{directory + dataset_name}/live_{current_round}.parquet",
     )

    # napi.download_dataset(f"{dataset_name}/validation_example_preds.parquet", f"{directory + dataset_name}/validation_example_preds.parquet")
    # napi.download_dataset(f"{dataset_name}/features.json", f"{directory + dataset_name}/features.json")

    print("Reading minimal training data")
    # read the feature metadata and get a feature set (or all the features)

    print("Open json file")
    with open(f"{directory + dataset_name}/features.json", "r") as f:
        feature_metadata = json.load(f)

    # features = list(feature_metadata["feature_stats"].keys()) # get all the features
    # features = feature_metadata["feature_sets"]["small"] # get the small feature set
    features = feature_metadata["feature_sets"][
        feature_set_name
    ]  # get the medium feature set
    target_cols = feature_metadata["targets"]
    # read in just those features along with era and target columns
    read_columns = features + target_cols + [ERA_COL, DATA_TYPE_COL]

    print("Set training data")
    # note: sometimes when trying to read the downloaded data you get an error about invalid magic parquet bytes...
    # if so, delete the file and rerun the napi.download_dataset to fix the corrupted file
    training_data = pd.read_parquet(
        f"{directory + dataset_name}/train.parquet", columns=read_columns
    )

    print("Set validation data")
    validation_data = pd.read_parquet(
        f"{directory + dataset_name}/validation.parquet", columns=read_columns
    )

    print("Set live data")
    live_data = pd.read_parquet(f"{directory + dataset_name}/live_{current_round}.parquet", columns=read_columns)

    # reduce the number of eras to every 4th era to speed things up... uncomment these lines to speed things up.
    # every_4th_era = training_data[ERA_COL].unique()[::4]
    # training_data = training_data[training_data[ERA_COL].isin(every_4th_era)]
    # every_4th_era = validation_data[ERA_COL].unique()[::4]
    # validation_data = validation_data[validation_data[ERA_COL].isin(every_4th_era)]

    print("Set all data")
    # get all the data to possibly use for training
    all_data = pd.concat([training_data, validation_data])

    # save indices for easier data selection later
    training_index = training_data.index
    validation_index = validation_data.index
    all_index = all_data.index

    print("Delete Data")
    # delete training and validation data to save space
    del training_data
    del validation_data
    gc.collect()  # clear up memory

    # Int8 datatype has pd.NA which don't play nice with models.  We simply fill NA with median values here
    print("cleaning up NAs")
    all_data[features] = all_data[features].fillna(all_data[features].median(skipna=True))
    all_data[features] = all_data[features].astype("int8")  # make sure change to float32 if using the non int8 data!
    live_data[features] = live_data[features].fillna(
        all_data[features].median(skipna=True)
    )  # since live data is only one era, we need to use the median for all eras

    live_data[features] = live_data[features].astype("int8")  # make sure change to float32 if using the non int8 data!
    # Alternatively could convert nan columns to be floats and replace pd.NA with np.nan

    print("Set Light GBM  Params")

    # small fast params
    params_name = "sm_lgbm"
    params = {"n_estimators": 2000,
              "learning_rate": 0.01,
              "max_depth": 5,
              "num_leaves": 2 ** 5,
              "colsample_bytree": 0.1}

    # recommended params
    # params_name = "lg_lgbm"
    # params = {
    #     "n_estimators": 20000,
    #     "learning_rate": 0.001,
    #     "max_depth": 6,
    #     "num_leaves": 2**6,
    #     "colsample_bytree": 0.1,
    # }


    # loop through all of our favorite targets and build models on each of them - one over training data, one over all available data
    # for the train_data models, we'll then predict on validation data
    # for the all_data models, we'll predict on live
    targets = [

        "target_jeremy_20",
        "target_ralph_20",
        "target_tyler_20",
        "target_victor_20",
        "target_waldo_20",
    ]
    prediction_cols = []



    for target in tqdm(targets):
        prediction_col = f"{params_name}_{dataset_name}_{feature_set_name}_{target}"
        train_data_model_name = f"train_data_{prediction_col}"
        print(f"Checking for existing model '{train_data_model_name}'")
        train_model = load_model(train_data_model_name)

        # Del lots here !!!!

        # predict on validation data
        all_data.loc[validation_index, prediction_col] = train_model.predict(
            all_data.loc[validation_index, features]
        )
        gc.collect()

        # do the same thing for all data (for predicting on live)
        all_data_model_name = f"all_data_{prediction_col}"
        print(f"Checking for existing model '{all_data_model_name}'")
        all_data_model = load_model(all_data_model_name)
        if not all_data_model:
            print(f"model not found, creating new one")
            all_data_model = LGBMRegressor(**params)
            all_data_target_index = (
                all_data.loc[all_index, target].dropna().index
            )  # make sure we only train on rows which have this target
            # train on all of train and save the model so we don't have to train next time
            all_data_model.fit(
                all_data.loc[all_data_target_index, features],
                all_data.loc[all_data_target_index, target],
            )
            print(f"saving new model: {all_data_model_name}")
            save_model(all_data_model, all_data_model_name)

        # predict on live data
        live_data[prediction_col] = all_data_model.predict(
            live_data[features].fillna(np.nan)
        )  # filling live data with nans makes us ignore those features if necessary
        gc.collect()

        prediction_cols.append(prediction_col)

    # make an ensemble
    all_data.loc[:, "equal_weight"] = all_data[prediction_cols].mean(axis=1)
    live_data["equal_weight"] = live_data[prediction_cols].mean(axis=1)

    prediction_cols.append("equal_weight")

    # make a 50% feature neutral variation of the ensemble model
    all_data["half_neutral_equal_weight"] = neutralize(
        df=all_data.loc[validation_index, :],
        columns=[f"equal_weight"],
        neutralizers=features,
        proportion=0.5,
        normalize=True,
        era_col=ERA_COL,
        verbose=True,
    )
    # do the same for live data
    live_data["half_neutral_equal_weight"] = neutralize(
        df=live_data,
        columns=[f"equal_weight"],
        neutralizers=features,
        proportion=0.5,
        normalize=True,
        era_col=ERA_COL,
        verbose=True,
    )

    prediction_cols.append("half_neutral_equal_weight")

    model_to_submit = f"half_neutral_equal_weight"

    # rename best model to "prediction" and rank from 0 to 1 to meet upload requirements
    all_data.loc[validation_index, "prediction"] = all_data.loc[
        validation_index, model_to_submit
    ].rank(pct=True)
    live_data["prediction"] = live_data[model_to_submit].rank(pct=True)
    all_data.loc[validation_index, "prediction"].to_csv(
        f"{directory + dataset_name}/validation_predictions_{current_round}.csv"
    )
    live_data["prediction"].to_csv(f"{directory + dataset_name}/live_predictions_{current_round}.csv")

    validation_example_preds = pd.read_parquet(
        f"{directory + dataset_name}/validation_example_preds.parquet"
    )
    all_data.loc[validation_index, EXAMPLE_PREDS_COL] = validation_example_preds[
        "prediction"
    ]

    # get some stats about each of our models to compare...
    # fast_mode=True so that we skip some of the stats that are slower to calculate
    validation_stats = validation_metrics(
        all_data.loc[validation_index, :],
        prediction_cols,
        example_col=EXAMPLE_PREDS_COL,
        fast_mode=True,
        target_col=TARGET_COL,
    )
    print(validation_stats[["mean", "sharpe"]].to_markdown())

    print(
        f"""
    Done! Next steps:
        1. Go to numer.ai/tournament (make sure you have an account)
        2. Submit validation_predictions_{current_round}.csv to the diagnostics tool
        3. Submit tournament_predictions_{current_round}.csv to the "Upload Predictions" button
    """
)


if __name__ == '__main__':
    main(str(596))