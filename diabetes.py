# -*- coding: utf-8 -*-
"""Diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YxOIIL5RedBVPJb0JiT57u7Sv60D4IJq

Objective

The objective of the dataset is to diagnostically predict whether a patient has diabetes based on certain diagnostic measurements included in the dataset.
"""

#Importing Libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

#Loading the dataset
df = pd.read_csv('/content/diabetes.csv')

df.head()

df.groupby('Outcome').mean()

# Seperating features and labels
X = df.drop(columns = 'Outcome', axis = 1)
Y = df['Outcome']

"""### Data Standardization"""

Scaler = StandardScaler()
Scaler.fit(X)
X = Scaler.transform(X)

X

# Train Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, stratify= Y, random_state = 2)
print(X.shape, X_train.shape, X_test.shape)

"""### Model Training"""

model = svm.SVC(kernel = 'linear')

model.fit(X_train, Y_train)

# Evaluation
predicted_Y = model.predict(X_test)
test_accuracy = accuracy_score(Y_test, predicted_Y)
print(test_accuracy)

"""### DL based model"""

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(units = 32, activation = 'relu', input_shape= [8]),
    layers.Dense(units = 32, activation = 'relu'),
    layers.Dense(units = 1, activation = 'sigmoid')
])

model.compile(
    loss = 'binary_crossentropy',
    optimizer = 'adam',
    metrics = ['binary_accuracy']
)

model.fit(
    X_train, Y_train,
    validation_data = (X_test, Y_test),
    batch_size = 32,
    epochs = 100
)