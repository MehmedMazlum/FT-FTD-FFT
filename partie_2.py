from homemadeFFT import *
import cmath
import math
import random
import numpy as np
import matplotlib.pyplot as plt


def signal(t):
    return 1.0*math.cos(3*math.pi*t) \
            +0.5*math.sin(10*math.pi*t) \
            

N=2**14
L=10.
deltat = L/N
x=[]
x1=[]
t=[]
for k in range(N):
    t.append(k*deltat)
for k in range(N):
    x1.append(1.0*math.cos(3*math.pi*t[k]))
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
plt.plot(omega[1:100],np.absolute(xhat[1:100]))
plt.show()


hhat=[]
beta=1./(9.*math.pi**2)
alpha=1./(10.*3.*math.pi)
hhat.append(0.)
for i in range(1,N):
    hhat.append(1j*alpha*omega[i]/(1+1j*alpha*omega[i]-beta*omega[i]**2))

plt.figure(figsize=(10,4))
plt.plot(omega,np.real(hhat))
plt.show()


yhat=[]
for i in range(0,N):
    yhat.append(hhat[i]*xhat[i])

y=invTF(yhat,L,N)

plt.figure(figsize=(10,4))
plt.plot(t,np.real(y))
plt.plot(t,x1)
plt.show()




   

