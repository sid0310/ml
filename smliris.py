#!/usr/bin/python3
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
iris=load_iris()
dir(iris)
iris.DESCR
iris.feature_names
iris.target_names
features=iris.data
label=iris.target
from sklearn.model_selection import train_test_split
train_data,test_data,label_train,label_test=train_test_split(features,label,test_size=0.1)
#calling desiciontree
clf=DecisionTreeClassifier()
trained=clf.fit(train_data,label_train)
p_flowers=trained.predict(test_data)
p_flowers #algo ans
label_test #act ans
# to find accurasy score
accuracy_score(label_test,p_flowers)