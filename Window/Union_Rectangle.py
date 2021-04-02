n=int(input())
X=[]
Y=[]
P=[]
imos=[[0]*(2*n+1) for i in range(2*n+1)]
ans=0

for i in range(n):
    x1,y1,x2,y2=map(int,input().split())
    X.append(x1)
    X.append(x2)
    Y.append(y1)
    Y.append(y2)
    P.append((x1,y1,1))
    P.append((x1,y2,-1))
    P.append((x2,y1,-1))
    P.append((x2,y2,1))
X.sort()
Y.sort()

for x,y,w in P:
    imos[X.index(x)+1][Y.index(y)+1]+=w

for i in range(1,2*n+1):
    for j in range(1,2*n+1):
        imos[i][j]+=imos[i-1][j]+imos[i][j-1]-imos[i-1][j-1]

for i in range(1,2*n+1):
    for j in range(1,2*n+1):
        if imos[i][j]:
            ans+=(X[i]-X[i-1])*(Y[j]-Y[j-1])

print(ans)
