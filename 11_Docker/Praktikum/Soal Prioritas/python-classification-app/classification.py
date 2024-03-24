from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import pandas as pd

df = pd.read_csv('akurasi_ekstraksi_ciri.csv')
df = df.fillna(0)

y = df['labels']
X = df.drop(['labels', 'path'], axis = 1)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#apply PCA
pca = PCA(n_components=4)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)

X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.25)

model = svm.SVC()
model.fit(X_train, y_train)

# predicting the response for test dataset
y_pred = model.predict(X_test)

# reporting model accuracy
print("Accuracy:", round(accuracy_score(y_test, y_pred)*100),'%')