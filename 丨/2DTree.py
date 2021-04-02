class kDTree():
    def __init__(self,n,points):
        self.count=0
        self.origin=points
        self.points=sorted(points)
        self.pointNum=[None]*n
        self.l=[None]*n
        self.r=[None]*n
        self.make2DTree(0,n,0)

    def make2DTree(self,l,r,depth):
        if not l<r:
            return None
        mid=(l+r)//2
        a=self.count
        self.count+=1

        if not depth&1:
            self.points[l:r]=sorted(self.points[l:r])
        else:
            self.points[l:r]=sorted(self.points[l:r],key=lambda x:x[1])
        self.pointNum[a]=mid
        self.l[a]=self.make2DTree(l,mid,depth+1)
        self.r[a]=self.make2DTree(mid+1,r,depth+1)
        return a

    def find(self,sx,tx,sy,ty):
        answer=[]
        def dfs(v,sx,tx,sy,ty,depth):
            x=self.points[self.pointNum[v]][0]
            y=self.points[self.pointNum[v]][1]
            if sx<=x and x<=tx and sy<=y and y<=ty:
                answer.append(self.origin.index(self.points[self.pointNum[v]]))
            if not depth&1:
                if self.l[v]!=None and sx<=x:
                    dfs(self.l[v],sx,tx,sy,ty,depth+1)
                if self.r[v]!=None and x<=tx:
                    dfs(self.r[v],sx,tx,sy,ty,depth+1)
            else:
                if self.l[v]!=None and sy<=y:
                    dfs(self.l[v],sx,tx,sy,ty,depth+1)
                if self.r[v]!=None and y<=ty:
                    dfs(self.r[v],sx,tx,sy,ty,depth+1)

        dfs(0,sx,tx,sy,ty,0)
        return sorted(answer)

n=int(input())
p=[]
for i in range(n):
    p.append(list(map(int,input().split())))
kDT=kDTree(n,p)
q=int(input())
for i in range(q):
    qry=list(map(int,input().split()))
    ans=kDT.find(qry[0],qry[1],qry[2],qry[3])
    for num in ans:
        print(num)
    print()
