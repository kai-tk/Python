import numpy as np
from numpy.linalg import matrix_power as nppow

"""
S=A+A^2+…+A^k

S_k=I+A+...+A^(k-1)
S=S_(k+1)-I

(A^k) = (A O)^k (I)
(S_k)   (I I)   (O)
"""

n,k,m=map(int,input().split())
a=[list(map(int,input().split())) for i in range(n)]
A=np.array(a)
O=np.zeros((n,n))
I=np.eye(n)

A=np.hstack((A,O))
I2=np.hstack((I,I))
A=np.vstack((A,I2))

Sk=nppow(A,k+1)
E,Sk=np.vsplit(Sk,n)
Sk,E=np.hsplit(Sk,n)

print((Sk-I)%m)
