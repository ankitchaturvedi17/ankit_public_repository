# -*- coding: utf-8 -*-
"""
Created on Tue May 22 20:42:13 2018

@author: Ankit
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('train.csv')

dataset = dataset.iloc[:,1:]
dataset = dataset.drop(['Name'],axis = 1)
dataset = dataset.drop(['Cabin'],axis = 1)


dataset = dataset.drop(['Ticket'],axis = 1)

dataset.mean()

dataset = dataset.fillna(dataset.mean())

dataset = dataset.dropna()

X= dataset.values


from sklearn.preprocessing import OneHotEncoder,LabelEncoder
labelencode = LabelEncoder() 
X[:,2] = labelencode.fit_transform(X[:, 2])
labelencode2 = LabelEncoder()
X[:,7] = labelencode2.fit_transform(X[:, 7])


onehot = OneHotEncoder()
X[:,7]= onehot.fit_transform(X[:,7]) 

y = X[:,0]
X= X[:,1:]

from sklearn.ensemble import RandomForestClassifier
Classifier = RandomForestClassifier(n_estimators = 10)

y=y.astype('int')

Classifier.fit(X,y)
#Fixing testData
testdata = pd.read_csv('test.csv')
testdata = testdata.drop(['Name'],axis = 1)
testdata = testdata.drop(['Cabin'],axis = 1)
testdata = testdata.drop(['Ticket'],axis = 1)


testdata.mean()

testdata = testdata.fillna(testdata.mean())

testdata = testdata.dropna()
testdata= testdata.values
test_passenger = testdata[:,0]
testdata = testdata[:,1:]

X_test= testdata
X_test[:,1] = labelencode.fit_transform(X_test[:, 1])
X_test[:,6] = labelencode2.fit_transform(X_test[:, 6])



y_pred = Classifier.predict(X_test)

final = pd.DataFrame(y_pred, test_passenger)

