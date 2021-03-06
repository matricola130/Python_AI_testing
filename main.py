import numpy as np
import sklearn
from sklearn import preprocessing
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

input_data = np.array([[2.1, -1.9, 5.5],
                       [-1.5, 2.4, 3.5],
                       [0.5, -7.9, 5.6],
                       [5.9, 2.3, -5.8]])

# PREPROCESSING TECHNIQUE

# Binariziamo i dati
data_binarized = preprocessing.Binarizer(threshold=0.5).transform(input_data)
print("\nBinarized data:\n", data_binarized)

# Mean Removal
print("------- MEAN REMOVAL --------")
print("Mean = ", input_data.mean(axis=0))
print("Std deviation = ", input_data.std(axis=0))

data_scaled = preprocessing.scale(input_data)
print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", data_scaled.std(axis=0))
print("-----------------------------")

# Scaling
print("----------SCALING -----------")
# Min/Max Scaling
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max scaled data:\n", data_scaled_minmax)
print("-----------------------------")

# Normalization
print("------- NORMALIZATION --------")
# Normalize Data
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
print("\nL1 normalized data:\n", data_normalized_l1)

# Normalize data
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nL2 normalized data:\n", data_normalized_l2)
print("-----------------------------")

# LABELING THE DATA

# Sample Input labels
input_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']

# Create label encoder
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

# encoding a set of labels
test_labels = ['green', 'red', 'black']
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels)
print("Encoded values =", list(encoded_values))

# decoding a set of values
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("Decoded labels =", list(decoded_list))
print("--------------------------------")
print("------CLASSIFIER------")


def classifier():
    # Prendiamo i dati dal dataset
    data = load_breast_cancer()

    # Organizziamo i dati
    label_names = data['target_names']
    labels = data['target']
    feature_names = data['feature_names']
    features = data['data']

    print(label_names)
    print(labels[0])
    print(feature_names[0])
    print(features[0])

    train, test, train_labels, test_labels = train_test_split(features, labels, test_size=0.40, random_state=42)

    #Building the model
    gnb = GaussianNB()
    model = gnb.fit(train, train_labels)

    #Evaluating model
    print("Predizione modello: ")
    preds = gnb.predict(test)
    print(preds)

    print("Accuracy score: ", accuracy_score(test_labels, preds))

    return


classifier()
