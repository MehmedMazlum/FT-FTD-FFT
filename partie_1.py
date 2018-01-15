from homemadeFFT import *
import cmath
import math
import random
import numpy as np
import matplotlib.pyplot as plt


def signal(t):
    return 1.0*math.cos(2*math.pi*t) \
            +0.5*math.cos(3*2*math.pi*t+math.pi/3) \
            +0.2*math.cos(5*2*math.pi*t+math.pi/5) \
            +0.2*math.cos(10*2*math.pi*t) \
            +2.0*math.cos(7*math.pi*t-math.pi/8)


N=1024*2*2*2*2
L=10.
deltat = L/N
x=[]
t=[]
for k in range(N):
    t.append(k*deltat)
for k in range(N):
    x.append(signal(t[k]))

plt.figure(figsize=(10,4))
plt.plot(t,x)
plt.show()


xhat=TF(x,L,N)

deltaomega = 2*math.pi/L
omega=[]
for k in range(0,int(N/2)+1):
    omega.append(deltaomega*k)
for k in range(int(N/2)+1,N):
    omega.append(-deltaomega*(N-k))


plt.figure(figsize=(10,4))
plt.plot(omega[1:200],np.absolute(xhat[1:200]))
plt.show()



