import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

# Reading the csv file and building a dataframe
data = pd.read_csv("projects/decision_trees/kyphosis.csv")
# Getting the dataframe top values
data.head()

# Retrieving info from the dataframe
data.describe()

# Visualizing data
sns.pairplot(data, hue="Kyphosis")

# Splitting data into labels and features
features = data.drop("Kyphosis", axis=1)
labels = data["Kyphosis"]

# Splitting the data into train and test sets
features_train, features_test, labels_train, labels_test = tts(features, labels,  test_size=0.3)

# Creating the classifier
classifier = DecisionTreeClassifier()
# Fitting the classifier
classifier.fit(features_train, labels_train)
# Predicting
prediction = classifier.predict(features_test)

# Evaluating the model
print(accuracy_score(labels_test, prediction))

# Report the metric values
print(classification_report(labels_test, prediction))

# Confusion Matrix
print(confusion_matrix(labels_test, prediction))
