"""
Weighted-Union-Find木
    WeightedUnionFind(n)でn個の要素を持つ親配列と重み配列を作成

    find(x):xの親を返す
    unite(x,y,w):yの重み-xの重み=wとなるようにxの属する木とyの属する木を併合
    same(x,y):xとyが同じ木に属するか判定
    diff(x,y):yの重み-xの重みを返す
    size(x):xの属する木の要素数
    members(x):xが属する木の要素のリスト
    roots(x):根のリスト
    group_count(x):木の数
    all_group_members:全ての木の要素のリスト
"""
class WeightedUnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n
        self.differ=[0]*n

    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            r=self.find(self.parents[x])
            self.differ[x]+=self.differ[self.parents[x]]
            self.parents[x]=r
            return self.parents[x]

    def unite(self,x,y,w):
        xp=self.find(x)
        yp=self.find(y)
        w=w+self.differ[x]-self.differ[y]

        if xp!=yp:
            if self.parents[xp]>self.parents[yp]:
                xp,yp=yp,xp
                w=-w

            self.parents[xp]+=self.parents[yp]
            self.parents[yp]=xp
            self.differ[yp]=w

    def same(self,x,y):
        return self.find(x)==self.find(y)

    def diff(self,x,y):
        xp=self.find(x)
        yp=self.find(y)
        if xp==yp:
            return True,self.differ[y]-self.differ[x]
        else:
            return False,0

    def size(self,x):
        return -self.parents[self.find(x)]

    def members(self,x):
        root=self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x<0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r:self.members(r) for r in self.roots()}



n,q=map(int,input().split())
WUF=WeightedUnionFind(n)
for i in range(q):
    query=list(map(int,input().split()))
    if query[0]==0:
        WUF.unite(query[1],query[2],query[3])
    elif query[0]==1:
        judge,diff=WUF.diff(query[1],query[2])
        if judge:
            print(diff)
        else:
            print("?")
