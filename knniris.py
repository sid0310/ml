from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt 
iris_data=load_iris()
iris_features=iris_data.data
#data with attribute
#extracting label as per features
label=iris_data.target
# to divide data for training 
from sklearn.model_selection import train_test_split
train_data,test_data,label_train,label_test=train_test_split(iris_features,label,test_size=0.5)
# importing knn classification
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=7)
trained=clf.fit(train_data,label_train)
data_predict=trained.predict(test_data)
print(accuracy_score(label_test,data_predict))