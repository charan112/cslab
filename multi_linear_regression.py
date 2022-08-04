import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
data=pd.read_csv('Z:\Y20CS085\CSLAB\mul_lin_regr.csv')
print(data)
x1=np.array(data['x1'])
x2=np.array(data['x2'])
x3=np.array(data['x3'])
y=np.asmatrix(data['y'])
y=y.transpose()
print(y)
unitmat=[]
for i in range(len(y)):
    unitmat.append(1)
x=np.column_stack((unitmat,x1,x2,x3))
xt=x.transpose()
xtx=np.dot(xt,x)
xty=np.dot(xt,y)
xtx_in=np.linalg.inv(xtx)
print(np.dot(xtx_in,xty))
