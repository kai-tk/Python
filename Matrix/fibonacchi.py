import numpy as np
from numpy.linalg import matrix_power as nppow

"""
F_n+1  =  (1 1)^n (1)
F_n       (1 0)   (0)
"""

n=int(input())
fib=[[1,1],[1,0]]
print(nppow(fib,n)[1][0])
