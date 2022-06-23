import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
data=pd.read_csv('Z:\Y20CS085\CSLAB\corelationcoeffnote.csv')
print(data.head())
x=np.array(data['x'])
y=np.array(data['y'])
xy=np.array(x*y)
xx=np.array(x*x)
yy=np.array(y*y)
num=len(x)*sum(xy)-(sum(x)*sum(y))
den=math.sqrt((len(x)*sum(xx)-(sum(x)*sum(x)))*(len(y)*sum(yy)-(sum(y)*sum(y))))
r=num/den
print("the corelation coeeficient is:",round(r*100,2))
