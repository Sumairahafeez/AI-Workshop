from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
iris = load_diabetes()
x = iris.data
y = iris.target
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=42)#0.2 ka matlab hai 2 hisson main divide kry ga pr 42 ka matlab ka 42 ky differnce sy kaam kray
#p = Pipeline([('scaler',StandardScaler()),
 #             ('model',LogisticRegression())])
model = LogisticRegression()
model.fit(X_train,y_train)
predictions = model.predict(X_test)
print("Accuracy: ",predictions)
