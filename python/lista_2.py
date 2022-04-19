from math import floor
import pandas as pd
from scipy.io import arff
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def readDataset():
    data = arff.loadarff('weather.nominal.arff')
    df = pd.DataFrame(data[0])
    df = df.applymap(str)
    df = df.applymap(lambda x: x.split('\'')[1])
    return df

def splitdataset(df):
    num = df.shape[0]
    x = df.values[:, 1:num]
    y = df.values[:, 0]
    X_train, X_test, y_train, y_test = train_test_split( 
    x, y, test_size = 0.3, random_state = 100)
    return x, y
def tarin_using_entropy(X_train, X_test, y_train):
  
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
            criterion = "entropy", random_state = 100,
            max_depth = 3, min_samples_leaf = 5)
  
    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy
  
  
# Function to make predictions
def prediction(X_test, clf_object):
  
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred
      
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
      
    print("Confusion Matrix: ",
        confusion_matrix(y_test, y_pred))
      
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)
      
    print("Report : ",
    classification_report(y_test, y_pred))
  
# Driver code
def main():
      
    # Building Phase
    data = readDataset()
    X, Y, X_train, X_test, y_train, y_test = splitdataset(data)
    clf_entropy = tarin_using_entropy(X_train, X_test, y_train)
      

      
    print("Results Using Entropy:")
    # Prediction using entropy
    y_pred_entropy = prediction(X_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)
