
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('train.csv')
# Deleting NA values
dataset = dataset.dropna()

#Selecting values from the dataset
X = dataset.iloc[:, 0:17].values
#y = dataset.iloc[:, 16].values


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


#Fixing Column A with label encoder
labelencoder_X_1 = LabelEncoder()
X = dataset.iloc[:, 0:17].values
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])

#Fixing column D with another label encoder
labelencoder_X_4 = LabelEncoder()
X[:, 4] = labelencoder_X_4.fit_transform(X[:, 4])
column4 = X[:,4]


#Fixing column E with another label encoder
labelencoder_X_5 = LabelEncoder()
X[:, 5] = labelencoder_X_5.fit_transform(X[:, 5])

#Fixing column F with another label encoder
labelencoder_X_6 = LabelEncoder()
X[:, 6] = labelencoder_X_6.fit_transform(X[:, 6])

#Fixing column G with another label encoder
labelencoder_X_7 = LabelEncoder()
X[:, 7] = labelencoder_X_7.fit_transform(X[:, 7])

#Fixing column I with another label encoder
labelencoder_X_9 = LabelEncoder()
X[:, 9] = labelencoder_X_9.fit_transform(X[:, 9])

#Fixing column J with another label encoder
labelencoder_X_10 = LabelEncoder()
X[:, 10] = labelencoder_X_10.fit_transform(X[:, 10])

#Fixing column L with another label encoder
labelencoder_X_12 = LabelEncoder()
X[:, 12] = labelencoder_X_12.fit_transform(X[:, 12])

#Fixing column M with another label encoder
labelencoder_X_13 = LabelEncoder()
X[:, 13] = labelencoder_X_13.fit_transform(X[:, 13])


#Using OneHotEncoder to fix values
#Implementing one hot encoder using categorical features
# Column D
onehotencoder_1 = OneHotEncoder(categorical_features = [4])
Train_X = onehotencoder_1.fit_transform(X).toarray()
# removing dummy variable
Train_X = Train_X[:,1:]

# Column E
onehotencoder_2 = OneHotEncoder(categorical_features = [6])
Train_X = onehotencoder_2.fit_transform(Train_X).toarray()
# removing dummy variable
Train_X = Train_X[:,1:]

# Column F
onehotencoder_3 = OneHotEncoder(categorical_features = [8])
Train_X = onehotencoder_3.fit_transform(Train_X).toarray()
# removing dummy variable
Train_X = Train_X[:,1:]


# Column G
onehotencoder_4 = OneHotEncoder(categorical_features = [21])
Train_X = onehotencoder_4.fit_transform(Train_X).toarray()
# removing dummy variable
Train_X = Train_X[:,1:]

# Column M
onehotencoder_5 = OneHotEncoder(categorical_features = [34])
Train_X = onehotencoder_5.fit_transform(Train_X).toarray()
# removing dummy variable
Train_X = Train_X[:,1:]


#cloumn 27 to be dropped-- Index 
#column 29 30 31 34 36 37
#using Standard Scaller to scale the data
X_train = Train_X
X_Index = X_train[:,27]



# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc1 = StandardScaler()
sc2 = StandardScaler()
sc3 = StandardScaler()
X_train[:,29:32] = sc1.fit_transform(X_train[:,29:32])

X_train[:,36:38] = sc2.fit_transform(X_train[:,36:38])

X_train[:,34:35] = sc3.fit_transform(X_train[:,34:35])

y_train = X_train[:,38]

X_train = np.delete(X_train,[27],1)
X_train = np.delete(X_train,[37],1)
#Creating Neural network
# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 25, init = 'uniform', activation = 'relu', input_dim = 37))

# Adding the second hidden layer
classifier.add(Dense(output_dim = 25, init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)

#Calling in testdata
#Now using only transform as fit is already used 

Test_dataset = pd.read_csv('test.csv')
# Deleting NA values
Test_dataset = Test_dataset.dropna()

#Selecting values from the dataset
X_test = Test_dataset.iloc[:, 0:17].values

X_test = Test_dataset.iloc[:, 0:17].values
X_test[:, 1] = labelencoder_X_1.transform(X_test[:, 1])

#Fixing column D with another label encoder

X_test[:, 4] = labelencoder_X_4.transform(X_test[:, 4])
column4 = X_test[:,4]


#Fixing column E with another label encoder
X_test[:, 5] = labelencoder_X_5.transform(X_test[:, 5])

#Fixing column F with another label encoder
X_test[:, 6] = labelencoder_X_6.transform(X_test[:, 6])

#Fixing column G with another label encoder
X_test[:, 7] = labelencoder_X_7.transform(X_test[:, 7])

#Fixing column I with another label encoder
X_test[:, 9] = labelencoder_X_9.transform(X_test[:, 9])

#Fixing column J with another label encoder
X_test[:, 10] = labelencoder_X_10.transform(X_test[:, 10])

#Fixing column L with another label encoder
X_test[:, 12] = labelencoder_X_12.transform(X_test[:, 12])

#Fixing column M with another label encoder
X_test[:, 13] = labelencoder_X_13.transform(X_test[:, 13])


yo = pd.DataFrame(X_test)
#Using OneHotEncoder to fix values
#Implementing one hot encoder using categorical features
# Column D
X_test = onehotencoder_1.transform(X_test).toarray()
# removing dummy variable
X_test = X_test[:,1:]

# Column E
X_test = onehotencoder_2.transform(X_test).toarray()
# removing dummy variable
X_test = X_test[:,1:]

# Column F
X_test = onehotencoder_3.transform(X_test).toarray()
# removing dummy variable
X_test = X_test[:,1:]


# Column G
X_test = onehotencoder_4.transform(X_test).toarray()
# removing dummy variable
X_test = X_test[:,1:]

# Column M
X_test = onehotencoder_5.transform(X_test).toarray()
# removing dummy variable
X_test = X_test[:,1:]


#cloumn 27 to be dropped-- Index 
#column 29 30 31 34 36 37
#using Standard Scaller to scale the data

X_Test_Index = X_test[:,27]



X_test[:,29:32] = sc1.transform(X_test[:,29:32])

X_test[:,36:38] = sc2.transform(X_test[:,36:38])

X_test[:,34:35] = sc3.transform(X_test[:,34:35])


X_test = np.delete(X_test,[27],1)


# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)
y_pred = y_pred.astype(int)

final = pd.DataFrame(y_pred, X_Test_Index)

final.to_csv('Submission.csv', sep=',')



