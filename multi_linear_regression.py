import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
x1=np.array(list(map(int,input().split())))
x2=np.array(list(map(int,input().split())))
y=np.asmatrix(list(map(int,input().split())))
y=y.transpose()
unitmat=[]
for i in range(len(x1)):
    unitmat.append(1)
x=np.column_stack((unitmat,x1,x2))
xt=x.transpose()
xtx=np.dot(xt,x)
xtx_in=np.linalg.inv(xtx)
xty=np.dot(xt,y)
b_cap=np.dot(xtx_in,xty)
print(*b_cap)
print("the required multi linear regression equation is Y=",b_cap[0],"+",b_cap[1],"X1 +",b_cap[2],"X2")
