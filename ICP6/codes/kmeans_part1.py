import dataset as dataset
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)


data = pd.read_csv('CC.csv')

# finding  Null values in the dataset
nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

data.loc[(data['MINIMUM_PAYMENTS'].isnull()==True),'MINIMUM_PAYMENTS']=data['MINIMUM_PAYMENTS'].mean()
data.loc[(data['CREDIT_LIMIT'].isnull()==True),'CREDIT_LIMIT']=data['CREDIT_LIMIT'].mean()


#elbow method to find the good no. of clusters
x = data.iloc[:,1:-1]
y = data.iloc[:,-1]


wcss = []
for i in range(1,7):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
print(wcss)
plt.plot(range(1,7),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

#Calculate the silhoutte score #n_clusters = 3
km = KMeans(n_clusters=3)
km.fit(x)
Y_cluster_kmeans= km.predict(x)
from sklearn import metrics
score = metrics.silhouette_score(x, Y_cluster_kmeans)
print(score)

# feature scaling
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x)

# Apply PCA.
x_scaler = scaler.transform(x)
pca = PCA(3)
x_pca = pca.fit_transform(x_scaler)
df2 = pd.DataFrame(data=x_pca)
finaldf = pd.concat([df2,data[['TENURE']]],axis=1)
# print(finaldf)

# KMeans after standarization

km = KMeans(n_clusters=3)
km.fit(x_pca)
Y_cluster_kmeans= km.predict(x_pca)
from sklearn import metrics
score = metrics.silhouette_score(x_pca, Y_cluster_kmeans)
print(score)
plt.scatter(x_pca[:, 0], x_pca[:, 1], c = Y_cluster_kmeans)
plt.show()
