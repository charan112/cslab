#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


# In[61]:


data=pd.read_csv('Downloads/problem1.csv')
print(data.head())
x=np.array(data['x'])
y=np.array(data['y'])
mx=sum(x)/len(x)
my=sum(y)/len(y)
num=0.0
for i in range(0,len(x)):
    num=num+(x[i]-mx)*(y[i]-my)
den=0.0
for i in range(0,len(x)):
    den=den+(x[i]-mx)*(x[i]-mx)
b1=num/den
b0=my-b1*mx
plt.plot(x,b1*x+b0)
print(b1)
print(b0)
plt.scatter(x, y, color = "m",marker = "o", s = 30)
plt.title('regression line')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:




