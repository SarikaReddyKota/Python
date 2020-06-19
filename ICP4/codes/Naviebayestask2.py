import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


train_df = pd.read_csv('./glass.csv')
test_df  = pd.read_csv('./glass.csv')
x_train =  test_df.drop("Type",axis=1)
y_train =  train_df["Type"]
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size = 0.3, random_state = 0)

Gaussian = GaussianNB()
Gaussian.fit(x_train, y_train)
y_pred =Gaussian.predict(x_test)
accuracy = round(Gaussian.score(x_test, y_test) * 100, 2)
print("accuracy is:", accuracy)
print("classification report is:", classification_report(y_test, y_pred))


