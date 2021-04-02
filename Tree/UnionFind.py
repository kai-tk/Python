"""
Union-Find木
    UnionFind(n)でn個の要素を持つ親配列を作成

    find(x):xの親を返す
    unite(x,y):xの属する木とyの属する木を併合
    same(x,y):xとyが同じ木に属するか判定
    size(x):xの属する木の要素数
    members(x):xが属する木の要素のリスト
    roots(x):根のリスト
    group_count(x):木の数
    all_group_members:全ての木の要素のリスト
"""
class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents=[-1]*n

    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]

    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)

        if x!=y:
            if self.parents[x]>self.parents[y]:
                x,y=y,x

            self.parents[x]+=self.parents[y]
            self.parents[y]=x

    def same(self,x,y):
        return self.find(x)==self.find(y)

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
