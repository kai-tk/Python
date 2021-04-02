import sys

def LIS(L,n):
  res=0
  dp=[1]*n
  for i in range(n):
    for j in range(i):
      if L[j]<L[i]:
        dp[i]=max(dp[i],dp[j]+1)
    res=max(res,dp[i])
  return res

def setParent(c,parent):
    if parent[c]!=float('inf'):
        setParent(parent[c],parent)
        parent[parent[c]]=c


sys.setrecursionlimit(100000)
data=input()
f=open(data,"r")

n=int(f.readline())
a=list(map(int,f.readline().split()))
parent=[float('inf')]*n
root=[[] for i in range(n)]

for i in range(n-1):
    l=list(map(int,f.readline().split()))
    if parent[l[1]-1]==float('inf'):
        parent[l[1]-1]=l[0]-1
    elif parent[l[0]-1]==float('inf'):
        parent[l[0]-1]=l[1]-1
    else:
        setParent(l[1]-1,parent)
        parent[l[1]-1]=l[0]-1

setParent(0,parent)
parent[0]=float('inf')

for i in range(1,n):
    c=parent[i]
    root[i].append(a[i])
    while(c!=0):
        if not root[c]:
            root[i].extend([a[c]])
            c=parent[c]
        else:
            root[i].extend(root[c])
            break

print(1)
for i in range(1,n):
    root[i].extend([a[0]])
    root[i].reverse()
    res=LIS(root[i],len(root[i]))
    print(res)
