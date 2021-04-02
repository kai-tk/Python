import numpy as np
from numpy.linalg import matrix_power as nppow

"""
G:全ての辺の長さが1の(有向)グラフ隣接行列

長さがkのパスの総数
    G_k=G^k
"""

n,k=map(int,input().split())
G=[[0]*n for i in range(n)]
for i in range(n):
    s=list(map(int,input().split()))
    if s[1]:
        for j in range(2,2+s[1]):
            G[i][s[j]-1]=1
print(np.count_nonzero(nppow(G,k))%10007)
