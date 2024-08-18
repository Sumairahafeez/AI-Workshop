from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.svm import SVC
# sklearn is a framework and has libraries linear model is a library
# all models work on finite data not infinite data s o we have to work with them
# it has conic section lying in it all conics have eccentricity from -1 to 1 so we have used -1,1 in reshape it will ocnvert it into 2d
x = np.array([5,15,25,35,45,55]).reshape((-1,1))# x is reshaped becuse it has many data
y = np.array([25,50,75,100,125,150])


p = Pipeline([('scaler',StandardScaler()),# if standard scaling is done after model it will create errors it is a tuple
              ('model',LinearRegression())])

p.fit(x,y)# it will train the model
print(p.predict([[100]]))
#pipeline is a queue FIFO
p2= Pipeline([('scaler',StandardScaler()),# if standard scaling is done after model it will create errors it is a tuple
              ('model',SVC())])# it works with vectors way it defines a resultant vector
p2.fit(x,y)
print(p2.predict([[100]]))
