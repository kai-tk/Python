"""
a^n(mod p)
"""
def power(a,n,p):
    bi = str(format(n,"b"))
    res = 1
    for i in range(len(bi)):
        res = (res*res) %p
        if bi[i] == "1":
            res = (res*a) %p
    return res
