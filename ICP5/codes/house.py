import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('train.csv')
train.SalePrice.describe()
print(train['GarageArea'], train['SalePrice'])

#scatter plot
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)
plt.scatter(train.GarageArea,train.SalePrice, alpha=.75, color='b')
plt.xlabel('train.GarageArea')
plt.ylabel('train.SalePrice')
plt.title('Simple Regression Model')
plt.show()

# deleting outliner data
fltr = train[(train.GarageArea < 1000) & (train.GarageArea >200)]
plt.scatter(fltr.GarageArea,fltr.SalePrice, alpha=.75, color='r')
plt.xlabel('train.GarageArea')
plt.ylabel('train.SalePrice')
plt.title('Simple Regression Model2')
plt.show()