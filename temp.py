import matplotlib.pyplot as plt
import numpy as np
import random as  rann
x=np.linspace(0,5,50)
xx=np.ones(50)
for i in range(50):
    xx[i]=1*rann.gauss(0,1)

y=2+4.5*x+xx
#plt.scatter(x, y)
alpha=.002
teta0=5
teta1=2
zx=sum(teta0+teta1*x-y)
zx=((teta0+teta1*x-y)*x)
j1=np.ones(100000)
for i in range(100000):
    teta0=teta0-alpha*.02*sum(teta0+teta1*x-y)
    teta1=teta1-alpha*.02*sum((teta0+teta1*x-y)*x)
    x1=(teta0+teta1*x-y)
    j1[i]=np.sqrt(np.sum(x1*x1))
plt.plot(j1)
    









