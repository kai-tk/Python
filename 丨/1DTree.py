class kDTree():
    def __init__(self,n,points):
        self.count=0
        self.origin=points
        self.points=sorted(points)
        self.pointNum=[None]*n
        self.l=[None]*n
        self.r=[None]*n
        self.make1DTree(0,n)

    def make1DTree(self,l,r):
        if not l<r:
            return None
        mid=(l+r)//2
        a=self.count
        self.count+=1
        self.pointNum[a]=mid
        self.l[a]=self.make1DTree(l,mid)
        self.r[a]=self.make1DTree(mid+1,r)
        return a

    def find(self,sx,tx):
        answer=[]
        def dfs(v,sx,tx):
            x=self.points[self.pointNum[v]]
            print(x)
            if sx<=x and x<=tx:
                answer.append(self.origin.index(self.points[self.pointNum[v]]))
            if self.l[v]!=None and sx<=x:
                dfs(self.l[v],sx,tx)
            if self.r[v]!=None and x<=tx:
                dfs(self.r[v],sx,tx)
        dfs(0,sx,tx)
        return sorted(answer)

n=int(input())
p=[]
for i in range(n):
    p.append(int(input()))
print(p)
kDT=kDTree(n,p)
print(kDT.find(2,5))
