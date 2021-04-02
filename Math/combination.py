import math

"""
階乗 n!
"""
def fact(n):
    return math.factorial(n)

"""
順列 nPr
"""
def perm(n,r):
    return math.factorial(n)//math.factorial(n-r)

"""
組み合わせ nCr
"""
def comb(n,r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

"""
重複組み合わせ nHr=(n+r-1)Cr
"""
def dup_comb(n,r):
    return comb(n+r-1,r)
