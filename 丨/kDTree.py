class kDTree():
    def __init__(self,n,points):
        self.count=0
        self.origin=points
        self.points=sorted(points)
        self.pointNum=[None]*n
        self.l=[None]*n
        self.r=[None]*n
        self.make2DTree(0,n)

    def make2DTree(self,l,r):
        if not l<r:
            return None
        mid=(l+r)//2
        a=self.count
        self.count+=1

        self.points[l:r]=sorted(self.points[l:r])
        self.pointNum[a]=mid
        self.l[a]=self.make2DTree(l,mid)
        self.r[a]=self.make2DTree(mid+1,r)
        return a

    def find(self,sx,tx):
        answer=[]
        def dfs(v,sx,tx):
            x=self.points[self.pointNum[v]][0]
            if sx<=x and x<=tx:
                answer.append(self.origin.index(self.points[self.pointNum[v]]))
            if self.l[v]!=None and sx<=x:
                dfs(self.l[v],sx,tx)
            if self.r[v]!=None and x<=tx:
                dfs(self.r[v],sx,tx,)

        dfs(0,sx,tx)
        return sorted(answer)

    def show(self):
        print(self.origin)

n=int(input())
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append([a,i])
    y.append([b,i])
xkDT=kDTree(n,x)
ykDT=kDTree(n,y)

q=int(input())
for i in range(q):
    qry=list(map(int,input().split()))
    #xkDT.show()
    #ykDT.show()
    xans=xkDT.find(qry[0],qry[1])
    yans=ykDT.find(qry[2],qry[3])
    ans=set(xans)&set(yans)
    for num in sorted(ans):
        print(num)
    print()
