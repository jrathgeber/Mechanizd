# -*- coding: utf-8 -*-

"""

Created on Tue Oct 29 15:13:15 2019

@author: Jason


"""



# Eras can be more or less applicable to other eras
# You can test this be splitting the eras into blocks of 10, training on each block, and evaluating on each other block.


eras10 = (eras // 10) * 10
print(eras10.value_counts())

results10 = []
for train_era, tdf in df[eras10<120].groupby(eras10):
    print(train_era)
    model = linear_model.LinearRegression()
    model.fit(tdf[features], tdf[target])
    for test_era, tdf in df[eras10<120].groupby(eras10):
        results10.append([
            train_era,
            test_era,
            correlation_score(tdf[target], model.predict(tdf[features]))
        ])


    
results_df = pandas.DataFrame(
    results10,
    columns=["train_era", "test_era", "score"]
).pivot(index="train_era", columns="test_era", values="score")
print(results_df)


# Each row here is the training block of eras, each column is a testing block of eras.
# Note that there is a period in the middle that does not seem to be relevant to other eras, and the
#  overall performance seems to decrease a bit over time.
plt.figure(figsize=(15,15))
plt.imshow(results_df, vmin=-0.04, vmax=0.04, cmap="RdYlGn")

