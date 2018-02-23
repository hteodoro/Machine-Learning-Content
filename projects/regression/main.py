
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression

# Reading the data from a csv file
data = pd.read_csv("projects/regression/titanic_train.csv")
# Getting the first data entries
data.head()

######## ANÁLISE EXPLORATÓRIA DE DADOS ########

# Retrieving some info about the data
data.info()
# Describing some data values
data.describe()

# Setting the figure's size
plt.figure(figsize=(10, 5))
# Getting some information about the data
sns.set_style('whitegrid')
# Comparing the amount of people that survived and didn't survive
sns.countplot(x="Survived", data=data)

# Making comparisons using sex values
sns.countplot(x="Survived", hue="Sex", data=data)

# Making comparisons using embarked values
sns.countplot(x="Survived", hue="Embarked", data=data)

######## LIMPEZA DE DADOS #########

# Defining value columns to integers (Sex, Embark)
sex = pd.get_dummies(data['Sex'], drop_first=True)
# Checking for the embarked values
print(data["Embarked"].value_counts())
# Changing embarked values to integers
embark = pd.get_dummies(data['Embarked'], drop_first=True)

# TODO: Normalize null age values
# Aumentando tamanho da figura
plt.figure(figsize=(12, 6))
# Relacionando idade com classe
sns.boxplot(x="Pclass", y="Age", data=data)

# Defining the method to fill the null age values
def fill_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return 37

        elif Pclass == 2:
            return 29

        else:
            return 24

    else:
        return Age

# Filling null age values with data
data["Age"] = data[["Pclass", "Age"]].apply(fill_age, axis=1)
# Printing the new configuration of the age column
print(data["Age"])
# Cleaning the null value in the embarked column
data.dropna(inplace=True)
# Dropping columns that are irrelevant for the model
data.drop(["Name", "Ticket", "Cabin"], axis=1, inplace=True)
# Adding columns pos constructed (sex, embarked)
data.drop(["Sex", "Embarked"], axis=1, inplace=True)
data = pd.concat([data, sex, embark], axis=1)

######## CONSTRUÇÃO DO MODELO ########
# Splitting the data into train and test sets
features = data.drop("Survived", axis=1)
labels = data["Survived"]
features_train, features_test, labels_train, labels_test = tts(features, labels, test_size=0.3)

# Creating the model, fitting it, and predicting on test values
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)
prediction = classifier.predict(features_test)

######## AVALIAÇÃO DO MODELO #######
# Evaluating the metrics to see how the model is doing
# Acurracy Score
print(accuracy_score(labels_test, prediction))
# Info report
print(classification_report(labels_test, prediction))
# Model Confusion Matrix
print(confusion_matrix(labels_test, prediction))
