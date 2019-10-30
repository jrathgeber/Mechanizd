# -*- coding: utf-8 -*-

"""

Created on Tue Oct 29 15:13:47 2019

@author: https://github.com/numerai/example-scripts/blob/master/analysis_and_tips.ipynb

"""


#Gotcha: Since the signal-to-noise ratio is so low, models can take many more iterations than expected, 
#and have scarily high in-sample performance



def our_score(preds, dtrain):
    return "score", -numpy.corrcoef(preds, dtrain.get_label())[0,1]

dtrain = xgboost.DMatrix(df1[features], df1[target])
dtest = xgboost.DMatrix(df2[features], df2[target])
dall = xgboost.DMatrix(df[features], df[target])


param = {
    'max_depth':3,
    'eta':0.1,
    'silent':1,
    'objective':'reg:linear',
    'eval_metric':'rmse',
    'nthread': -1,
}
evals_result = {}
bst = xgboost.train(
    params=param,
    dtrain=dtrain,
    feval=our_score,
    num_boost_round=1000,
    evals=[(dtrain, 'train'), (dtest, 'test')],
    evals_result=evals_result,
    verbose_eval=10,
)

(0.5 - 0.57*pandas.DataFrame({k: v['score'] for k,v in evals_result.items()})).plot()

(-pandas.DataFrame({k: v['score'] for k,v in evals_result.items()})).plot(ylim=[0,0.045])

