# -*- coding: utf-8 -*-

import xgboost as xgb
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn import metrics

import warnings

names = ('bernie', 'ken') 

def main():

    warnings.filterwarnings("ignore")
    
    print("\n# Loading Numerai Sata...")

    for name in names:
        
        target = "target_" +  name
        submission = name + "_submission.csv"        
                
        # The training data is used to train your model how to predict the targets.
        train = pd.read_csv('C:\dep\\numerai2\\numerai_training_data.csv', header=0)
        
        # The tournament data is the data that Numerai uses to evaluate your model.
        tournament = pd.read_csv('C:\dep\\numerai2\\numerai_tournament_data.csv', header=0)
    
        # The tournament data contains validation data, test data and live data.
        # Validation is used to test your model locally so we separate that.
        validation = tournament[tournament['data_type']=='validation']
    
        # There are five targets in the training data which you can choose to model using the features.
        # Numerai does not say what the features mean but that's fine; we can still build a model.
        # Here we select the bernie_target.
        train_bernie = train.drop([
            'id', 'era', 'data_type',
            'target_charles', 'target_elizabeth',
            'target_jordan', 'target_ken'], axis=1)
    
        # Transform the loaded CSV data into numpy arrays
        features = [f for f in list(train_bernie) if "feature" in f]
        X_train = train_bernie[features]
        y_train = train_bernie[target]
        X_test = validation[features]
        y_test = validation[target]
        
        ids = tournament['id']
        
        # Need Xg Boot here
        xg_reg = xgb.XGBRegressor(objective ='reg:linear', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 6, alpha = 10, n_estimators = 10)
        xg_reg.fit(X_train,y_train)
        preds = xg_reg.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        
        print("RMSE: %f" % (rmse))
        print("- preds " , preds)
    
        # Based on the model we can predict the probability of each row being
        # a bernie_target in the validation data.
        # The model returns two columns: [probability of 0, probability of 1]
        # We are just interested in the probability that the target is 1.
        # y_prediction = preds
        #probabilities = y_prediction[:, 1]
        probabilities = preds
        print("- probabilities:", probabilities[1:6])
    
        # We can see the probability does seem to be good at predicting the
        # true target correctly.
        print("- target : \n", validation[target][1:10])
        
        print("- rounded probability:", [round(p) for p in probabilities][1:6])
    
        # But overall the accuracy is very low.
        correct = [round(x)==y for (x,y) in zip(probabilities, validation[target])]
        print("- accuracy: ", sum(correct)/float(validation.shape[0]))
    
        # The targets for each of the tournaments are very correlated.
        tournament_corr = np.corrcoef(validation[target], validation['target_elizabeth'])
        print("- bernie vs elizabeth corr:", tournament_corr)
        # You can see that target_elizabeth is accurate using the bernie model as well.
        correct = [round(x)==y for (x,y) in zip(probabilities, validation['target_elizabeth'])]
        print("- elizabeth using bernie:", sum(correct)/float(validation.shape[0]))
    
        # Numerai measures models on logloss instead of accuracy. The lower the logloss the better.
        # Numerai only pays models with logloss < 0.693 on the live portion of the tournament data.
        # Our validation logloss isn't very good.
        print("- validation logloss:", metrics.log_loss(validation[target], probabilities))
    
        # To submit predictions from your model to Numerai, predict on the entire tournament data.
        x_prediction = tournament[features]
        
        #y_prediction = model.predict_proba(x_prediction)
        preds = xg_reg.predict(x_prediction)
            
        #results = y_prediction[:, 1]
        results = preds
    
        print("# Creating submission...")
        # Create your submission
        results_df = pd.DataFrame(data={'probability':results})
        joined = pd.DataFrame(ids).join(results_df)
        print("- joined:", joined.head())
    
        print("# Writing predictions to bernie_submissions.csv...")
        # Save the predictions out to a CSV file.
        joined.to_csv(submission, index=False)
        # Now you can upload these predictions on https://numer.ai



if __name__ == '__main__':
    main()