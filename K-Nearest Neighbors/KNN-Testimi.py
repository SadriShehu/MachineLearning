import pandas as pd
from sklearn.cross_validation import train_test_split
Data = pd.read_csv("DataFrame.csv")

X = Data.drop('AQI Category',1)
Y = Data['AQI Category']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,train_size=0.7,random_state=7)

objKNN = KNN(3)
objKNN.trajnoAlgoritmin(X_train,Y_train)
objKNN.prediko(X_test)
objKNN.predikimet()
objKNN.saktesiaAlgoritmit(Y_test)
