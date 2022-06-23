import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
data=pd.read_csv('Z:\Y20CS085\CSLAB\prob3.csv')
print(data.head())
x=np.array(data['x'])
y=np.array(data['y'])
print(x,y)
mx=sum(x)/len(x)
my=sum(y)/len(x)
num=0
den=0
for i in range(0,len(x)):
    for j in range(0,len(y)):
                   num=num+((x[i]-mx)*(y[j]-my))
                   den=den+((x[i]-mx)*(x[i]-mx))*((y[j]-my)*(y[j]-my))
ro=num/math.sqrt(den)
print(ro)
