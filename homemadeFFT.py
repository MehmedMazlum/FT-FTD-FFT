import cmath

def TFD(x,N):
    
    y=[]
    alpha=cmath.exp(-1j*2*cmath.pi/N)
    for i in range(0,N):
        sum=complex(0.,0)
        for j in range(0,N):
            sum=sum+alpha**(j*i)*x[j]
        y.append(sum/N)
    return y
    
def FFT(x,N):

    p1=[]
    p2=[]
    y=[]
    Ns2=int(N/2)
    alpha=cmath.exp(-1j*cmath.pi/Ns2)
    if N==2:
        y.append(0.5*(x[0]+x[1]))
        y.append(0.5*(x[0]-x[1]))
    else:
        for i in range(0,Ns2):
            p1.append(x[2*i])
            p2.append(x[2*i+1])
        
        p3=FFT(p1,Ns2)
        p4=FFT(p2,Ns2)
        
        for i in range(0,Ns2):
            y.append(0.5*p3[i]+0.5*alpha**i*p4[i])
        for i in range(0,Ns2):
            y.append(0.5*p3[i]-0.5*alpha**i*p4[i])

    return y

def invFFT(x,N):

    y=[]
    p=FFT(x,N)
    for i in range(0,N):
        p[i]=N*p[i]
    y.append(p[0])  
    for i in range(1,N):
        y.append(p[N-i].conjugate())

    return y


def f(x):
    #return x*cmath.exp(-x)
    return cmath.cos(x)

def fhat(x):
    return 1./pow(1+1j*x,2)

def sample(L,N):
    y=[]
    for i in range(0,N):
        y.append(f(i*L/N))
    return y

def sampletf(L,N):
    y=[]
    for i in range(0,int(N/2)):
        y.append(fhat(2*cmath.pi*i/L))
    y.append(fhat(cmath.pi*N/L))
    for i in range(1,int(N/2)):
        y.append(fhat(-2*cmath.pi*(N/2-i)/L))
    return y

def TF(x,L,N):
    y=[]
    y=FFT(x,N)
    y=[L*i for i in y]
    return y

def invTF(x,L,N):
    y=[]
    y=invFFT(x,N)
    for i in range(0,N):
      y[i]=y[i]/L
    return y