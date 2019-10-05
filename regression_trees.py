import pandas as pd 

import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

%matplotlib inline
df = pd.read_csv("final.csv", sep=";")
df.head()
colList = []
for i in df.columns:
    if i.startswith('SNP'):
        colList.append(i)
        
        
for i in colList:
    df[i] = df[i].factorize()[0]
    
feats = colList + ["SEX_y", "Age_index"]

X = df[feats].values
y = df["log_BMI"].values

model = DecisionTreeRegressor(max_depth=100)
scores = cross_val_score(model, X, y, cv=5, scoring="neg_mean_absolute_error")
np.mean(scores), np.std(scores)