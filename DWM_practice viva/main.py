import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

# Load dataset
dataset = pd.read_csv("Data - Data.csv")
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Handling missing data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

# Encoding categorical data in independent variable
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

# Encoding dependent variable
le = LabelEncoder()
y = np.array(le.fit_transform(y))

# Splitting the dataset into the training set and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Feature scaling
sc = StandardScaler()
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.transform(x_test[:, 3:])

# Training the Decision Tree classifier on the training set
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
classifier.fit(x_train, y_train)

# Making predictions on the test set
predictions = classifier.predict(x_test)
print(predictions)

# Evaluating accuracy
accuracy = classifier.score(x_test, y_test)
print(f"Accuracy: {accuracy}")

# Displaying the test set results
print("Test Set Actual Values:")
print(y_test)