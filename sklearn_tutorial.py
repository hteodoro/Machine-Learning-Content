from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score

# First step: loading the data
wine_data_frame = datasets.load_wine()
# Second step: Splitting the data
features = wine_data_frame.data
labels = wine_data_frame.target
# Third step: Separating training and testing data
train_features, test_features, train_labels, test_labels = tts(features, labels, test_size = 0.20)
# Fourth step: Building the classifier
classifier = svm.SVC(kernel='linear') ### Support Vector Classification ###
# Fifth step: Training the classifier
classifier.fit(train_features, train_labels)
# Sixth step: Predicting data
prediction = classifier.predict(test_features)
print(prediction)
# Seventh step: Evaluate the model
accuracy = accuracy_score(test_labels, prediction)
print("accuracy: {}".format(accuracy))
