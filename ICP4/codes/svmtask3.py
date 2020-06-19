import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


train_df = pd.read_csv('./glass.csv')
test_df  = pd.read_csv('./glass.csv')
x_train =  test_df.drop("Type",axis=1)
y_train =  train_df["Type"]
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size = 0.3, random_state = 0)

svc = SVC()
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
acc_svc = round(svc.score(x_test, y_test) * 100, 2)
print("svm accuracy is:", acc_svc)
print("classification report is:", classification_report(y_test, y_pred))


