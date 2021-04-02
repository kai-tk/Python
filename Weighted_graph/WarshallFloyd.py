INFTY=float('inf')

def warshallFloyd(l,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                l[i][j]=min(l[i][j],l[i][k]+l[k][j])
    return l

n,e=map(int,input().split())
l=[[INFTY for i in range(n)] for i in range(n)]
for i in range(n):
    l[i][i]=0

for i in range(e):
    a,b,c=map(int,input().split())
    l[a][b]=c

distance=warshallFloyd(l,n)

negative=False

for i in range(n):
    if l[i][i]<0:
        negative=True
        break

if negative:
    print("NEGATIVE CYCLE")
else:
    for i in range(n):
        for j in range(n):
            if j:
                print(" ",end='')
            if l[i][j]==INFTY:
                print("INF",end='')
            else:
                print(l[i][j],end='')
        print()
