# -*- coding: utf-8 -*-

"""

Created on Mon Nov 11 16:04:43 2019

@author: Jason

"""

#__ORIGINAL author__ = 'Nick Sarris (ngs5st)'

#import umap
import time
import os
import numpy as np
import pandas as pd
import xgboost as xgb
#import lightgbm as lgb
import operator
import random

from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from sklearn.base import TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline

from sklearn.model_selection import KFold
from sklearn.ensemble import ExtraTreesRegressor

TOURNAMENT_NAME = "kazutsugi"
TARGET_NAME = "target_kazutsugi"
PREDICTION_NAME = "prediction_kazutsugi"

BENCHMARK = 0.002
BAND = 0.04

# Submissions are scored by spearman correlation
def score(df):
   
    return np.corrcoef( df[TARGET_NAME], df[PREDICTION_NAME].rank(pct=True, method="first") )[0,1]

# The payout function
def payout(scores):
    return ((scores - BENCHMARK)/BAND).clip(lower=-1, upper=1)


class GenerateLinear(TransformerMixin):

    def __init__(self, n_neighbors, max_elts=None):
        self.rnd = 2019
        self.n = n_neighbors
        self.max_elts = max_elts
        self.verbose = True
        self.neighbors = []
        self.clfs = []

    def fit(self, X, y):
        random.seed(self.rnd)
        if self.max_elts == None:
            self.max_elts = len(X.columns)

        list_vars = list(X.columns)
        random.shuffle(list_vars)
        lastscores = (np.zeros(self.n) + 1e15)
        for elt in list_vars:
            self.neighbors.append([elt])

        for elt in list_vars:
            index = 0
            scores = []
            print('Currently Estimating {}'.format(elt))

            for elt2 in self.neighbors:
                if len(elt2) < self.max_elts:
                    clf1 = LinearRegression(fit_intercept=False,
                        normalize=True, copy_X=True, n_jobs=-1)
                    clf1.fit(X[elt2 + [elt]], y)
                    scores.append(mean_squared_error(y, clf1.predict(X[elt2 + [elt]])))
                    index += 1
                else:
                    scores.append(lastscores[index])
                    index += 1

            gains = lastscores - scores
            temp = gains.argmax()
            lastscores[temp] = scores[temp]
            self.neighbors[temp].append(elt)

        index = 0
        for elt in self.neighbors:
            clf = LinearRegression(fit_intercept=False,
                normalize=True, copy_X=True, n_jobs=-1)
            clf.fit(X[elt], y)
            self.clfs.append(clf)
            if self.verbose:
                print(index, lastscores[index], elt)
            index += 1

    def transform(self, X):
        index = 0
        for elt in self.neighbors:
            X['neighbor' + str(index)] = \
                self.clfs[index].predict(X[elt])
            index += 1
        return X

    def fit_transform(self, X, y=None, **fit_params):
        self.fit(X,y)
        return self.transform(X)

class GeneratePCA():

    def __init__(self):
        self.n_comp = 5
        self.pca = PCA(n_components=self.n_comp)

    def fit(self, X=None, y=None):
        return self.pca.fit(X)

    def transform(self, X, output):
        pca_results = self.pca.transform(
            normalize(X, axis=0))
        for i in range(0, self.n_comp):
            output['pca_' + str(i)] = pca_results[:, i]
        return output

    def fit_transform(self, X, output):
        self.pca.fit(X)
        pca_results = self.pca.transform(
            normalize(X, axis=0))
        for i in range(0, self.n_comp):
            output['pca_' + str(i)] = pca_results[:, i]
        return output

class XgbWrapper(object):

    def __init__(self, seed=2018, params=None):
        self.param = params
        self.param['seed'] = seed
        self.nrounds = params.pop('nrounds', 200)

    def train(self, x_train, y_train):
        dtrain = xgb.DMatrix(x_train, label=y_train)
        self.gbdt = xgb.train(self.param, dtrain, self.nrounds)

    def predict(self, x):
        return self.gbdt.predict(xgb.DMatrix(x))

def seed_everything(seed=1235):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)

def SelectFeatures(X, y, cutoff):

    clf = xgb.XGBClassifier(n_estimators=20, base_score=0.005)
    clf.fit(X, y)

    column_importance = clf.feature_importances_
    columns = X.columns
    column_dict = dict()
    column_list = []

    for row, value in zip(columns, column_importance):
        column_dict[row] = value

    column_dict = sorted(column_dict.items(), key=operator.itemgetter(1))
    for row, value in column_dict:
        print ('Feature:', row,'| Importance:', value)
        if value > cutoff:
            list.append(column_list, row)

    return column_list

def get_oof(clf, ntrain, ntest, kf, train, labels, test):

    oof_train = np.zeros((ntrain,))
    oof_test = np.zeros((ntest,))
    oof_test_skf = np.empty((5, ntest))

    for i, (train_index, test_index) in enumerate(kf):
        x_tr = train[train_index]
        y_tr = labels[train_index]
        x_te = train[test_index]

        clf.train(x_tr, y_tr)
        oof_train[test_index] = clf.predict(x_te)
        oof_test_skf[i, :] = clf.predict(test)

    oof_test[:] = oof_test_skf.mean(axis=0)
    return oof_train.reshape(-1, 1), oof_test.reshape(-1, 1)

def main():

    print("Loading Data ...")
    ###################################################

    directory = "F://Numerai//numerai185//"
    train_df = pd.read_csv(directory + 'numerai_training_data.csv')
    test_df = pd.read_csv(directory + 'numerai_tournament_data.csv')

    print("Initial Processing ...")
    ###################################################

    ids = test_df['id'].values
    labels = pd.DataFrame(train_df['target_kazutsugi'].values)
    cols_to_drop = ["id", "era", "data_type", "target_kazutsugi"]

    for col in cols_to_drop:
        train_df.drop(col, inplace=True, axis=1)
        if col in test_df.columns:
            test_df.drop(col, inplace=True, axis=1)

    print("Specifying Initial Features ...")
    ###################################################

    combined_features = []
    attributes = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

    for attribute in attributes:
        print("\nTraining on Attribute: {}".format(attribute.capitalize()))
        feature_df = train_df[[col for col in train_df.columns if attribute in col]]
        important_cols = SelectFeatures(feature_df, labels, 0.01)
        combined_features += important_cols

    print("Limit Features ...")
    ###################################################

    train_feats = train_df[combined_features]
    test_feats = test_df[combined_features]

    print("Generate Linear Neighbors ...")
    ###################################################

    linear_feats = GenerateLinear(n_neighbors=train_feats.shape[1], max_elts=2)
    train_feats = linear_feats.fit_transform(train_feats, labels)
    test_feats = linear_feats.transform(test_feats)

    print("Scaling Columns ...")
    ###################################################

    train_feats = train_feats[important_cols]
    test_feats = test_feats[important_cols]
    pipeline = Pipeline([('scaler', MinMaxScaler())])
    poly_train = pd.DataFrame(pipeline.fit_transform(train_feats))
    poly_test = pd.DataFrame(pipeline.transform(test_feats))

    print("Generating PCA ...")
    ###################################################

    pca_feats = GeneratePCA()
    train_feats = pca_feats.fit_transform(train_feats, poly_train)
    test_feats = pca_feats.transform(test_feats, poly_test)

    print("Training First Layer ...")
    ###################################################

    train = np.array(train_feats)
    test = np.array(test_feats)
    labels = np.array(labels)

    ntrain = train.shape[0]
    ntest = test.shape[0]
    kf = KFold(n_splits=5, shuffle=True, random_state=2018).split(train)

    xgb_params = {}
    xgb_params["objective"] = "reg:squarederror"
    xgb_params["eta"] = 0.05
    xgb_params["subsample"] = 0.7
    xgb_params["silent"] = 1
    xgb_params["max_depth"] = 5
    xgb_params["min_child_weight"] = 5
    xgb_params['eval_metric'] = 'rmse'

    xg = XgbWrapper(seed=2019, params=xgb_params)
    xg_oof_train, xg_oof_test = get_oof(xg, ntrain, ntest, kf, train, labels, test)
    #print("XG-CV: {}".format(roc_auc_score(labels, xg_oof_train)))
        
    
    print("Generating metrics...")
    ###################################################
    
    # training_data[PREDICTION_NAME] = model.predict(training_data[feature_names])
    # tournament_data[PREDICTION_NAME] = model.predict(tournament_data[feature_names])    
    
    # train[PREDICTION_NAME] = xgb_model.predict(xgb.DMatrix(train[features], feature_names = features) )
    # tournament[PREDICTION_NAME] = xgb_model.predict(xgb.DMatrix(tournament[features], feature_names = features) )

    train_df[PREDICTION_NAME] = xg.predict(train_df[combined_features] )
    test_df[PREDICTION_NAME] = xg.predict(test_df[combined_features] )
    
    # Check the per-era correlations on the training set
    train_correlations = train_df.groupby("era").apply(score)
    
    # train_correlations = xg_oof_train.groupby("era").apply(score)
        
    print(f"On training the correlation has mean {train_correlations.mean()} and std {train_correlations.std()}")
    print(f"On training the average per-era payout is {payout(train_correlations).mean()}")
            
    
    # Check the per-era correlations on the validation set
    validation_data = test_df[test_df.data_type == "validation"]
    validation_correlations = validation_data.groupby("era").apply(score)
    
    # validation_correlations = xg_oof_test.groupby("era").apply(score)
    
    print(f"On validation the correlation has mean {validation_correlations.mean()} and std {validation_correlations.std()}")
    print(f"On validation the average per-era payout is {payout(validation_correlations).mean()}")
           
    print("Generate Submission ...")
    ###################################################

    submission = pd.DataFrame()
    submission['id'] = ids
    submission['prediction_kazutsugi'] = xg_oof_test
    submission.to_csv("F:\\Numerai\\numerai" + 185 + "\\" + "output_sarris.csv", index=False)

if __name__ == "__main__":
    main()