import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
#this is for apple and orange
features=[[100,0],[120,0],[130,1],[140,1]]
#here 0= smooth for apple and 1= bumpy for orange
label=["appel","appel","orange","orange"]
#decision tree classifier
clf=DecisionTreeClassifier()
trained=clf.fit(features,label)
# traning the data
trained.predict([[123,1]])