import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import linear_model

train = pd.read_csv('winequality-red.csv')
numeric_features = train.select_dtypes(include=[np.number])
# Finding the top 3 most correlated features to target label
corr = numeric_features.corr()
print (corr['quality'].sort_values(ascending=False)[:3], '\n')

# deleting Null values in the dataset
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

#handling the missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(data.isnull().sum() != 0))

#Build a linear model
y = np.log(train.quality)
X = data.drop(['quality'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(
                                    X, y, random_state=42, test_size=0.33)


lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
##Evaluate the performance and visualize results
print ("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))