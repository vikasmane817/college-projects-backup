
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O 



import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


mushroom = pd.read_csv('mushrooms.csv')
mushroom.info()
#pulling the first five rows of dataset
mushroom.head(5).transpose()
#checking for null values
mushroom.isna().sum()
#checking for duplicates
mushroom.duplicated().sum()
#checking for unique value counts
for i in mushroom.columns:
    print(mushroom[str(i)].value_counts())
    print('\n')
#generating dummy variable through one-hot encoding
mushroom_en = pd.get_dummies(mushroom, drop_first = True)
mushroom_en.shape
mushroom_en.columns

#splitting the dataset
X_feature = list(mushroom_en.columns)
X_feature.remove('class_p')
X = mushroom_en[X_feature]
X.columns

Y = mushroom_en['class_p']
Y.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size = 0.30, random_state = 42)

print("X_train.shape",X_train.shape)
print("X_test.shape",X_test.shape)
print("y_train.shape",y_train.shape)
print("y_test.shape",y_test.shape)

#We'll go through the indivisual models one by one
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 21)
knn.fit(X_train, y_train)

#predicting for test data
knn_test_pred = knn.predict(X_test)

#evaluate the model
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, knn_test_pred))

pd.crosstab(y_test, knn_test_pred, rownames = ['Actual'], colnames= ['Predictions'])

#error on train data
knn_train_pred = knn.predict(X_train)
print(accuracy_score(y_train, knn_train_pred))

pd.crosstab(y_train, knn_train_pred, rownames = ['Actual'], colnames = ['Predictions'])

# creating empty list variable 
acc = []

# running KNN algorithm for 3 to 50 nearest neighbours(odd numbers) and 
# storing the accuracy values

for i in range(3,50,2):
    neigh = KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train, y_train)
    train_acc = np.mean(neigh.predict(X_train) == y_train)
    test_acc = np.mean(neigh.predict(X_test) == y_test)
    acc.append([train_acc, test_acc])


import matplotlib.pyplot as plt # library to do visualizations 

# train accuracy plot 
plt.plot(np.arange(3,50,2),[i[0] for i in acc],"ro-")
