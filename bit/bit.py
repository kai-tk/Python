"""
    showBit(n):nを2進数表示
    bitCheck(n,i):nのi桁目を返す
    bitOn(n,i):nのi桁目を1にする
    bitOff(n,i):nのi桁目を0にする
    bitFlip(n,i):nのi桁目を反転する
    isbitAll(n):nが(1<<64)-1か判定
    isbitAny(n):nが0でないか判定
    isbitNone(n):nが0か判定
    bitCount(n):nの1の数を判定
"""
def showBit(n):
    print("{:b}".format(n))

def bitCheck(n,i):
    return (int(bool(n&1<<i)))

def bitOn(n,i):
    return n|1<<i

def MaskOn(n,m):
    return n|m

def bitOff(n,i):
    return n&~(1<<i)

def MaskOff(n,m):
    return n&~m

def bitFlip(n,i):
    return n^1<<i

def MaskFlip(n,m):
    return n^m

def isbitAll(n):
    return int(bitCount(~n)==0)

def isMaskAll(n,m):
    return int(bitCount(~n&m)==0)

def isbitAny(n):
    return int(bitCount(n)>0)

def isMaskAny(n,m):
    return int(bitCount(n&m)>0)

def isbitNone(n):
    return int(bitCount(n)==0)

def isMaskNone(n,m):
    return int(bitCount(n&m)==0)

def bitCount(n):
    return bin(n).count('1')

def MaskCount(n,m):
    return bitCount(n&m)



b=0
masks=[]
n=int(input())
for i in range(n):
    mask=0
    m=list(map(int,input().split()))
    for j in range(m[0]):
        mask=bitOn(mask,m[j+1])
    masks.append(mask)

q=int(input())
for i in range(q):
    qry=list(map(int,input().split()))
    if qry[0]==0:
        print(bitCheck(b,qry[1]))
    elif qry[0]==1:
        b=MaskOn(b,masks[qry[1]])
    elif qry[0]==2:
        b=MaskOff(b,masks[qry[1]])
    elif qry[0]==3:
        b=MaskFlip(b,masks[qry[1]])
    elif qry[0]==4:
        print(isMaskAll(b,masks[qry[1]]))
    elif qry[0]==5:
        print(isMaskAny(b,masks[qry[1]]))
    elif qry[0]==6:
        print(isMaskNone(b,masks[qry[1]]))
    elif qry[0]==7:
        print(MaskCount(b,masks[qry[1]]))
    elif qry[0]==8:
        print(b&masks[qry[1]])
