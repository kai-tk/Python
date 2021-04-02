"""
Segment-Tree
    add_query(p,q,x):[p,q]にxを足す
    find_query(i):iの値
"""

class SegmentTree():
    def __init__(self,n):
        self.offset=self.setOffset(n)
        self.segTree=[0]*(2*self.offset+1)
        self.lazyTree=[0]*(2*self.offset+1)

    def setOffset(self,n):
        if n==1:
            return 1
        else:
            return 2**(n-1).bit_length()-1

    def lazyIndex(self,p,q):
        if p==0 and q==self.offset:
            return
        L=p+self.offset
        R=q+self.offset
        l=(L-1)//2
        r=(R-1)//2
        Lflag=False
        Rflag=False
        while l<r:
            if Rflag or R&1:
                Rflag=True
                yield r
            if Lflag or not L&1:
                Lflag=True
                yield l
            L=l
            R=r
            l=(L-1)//2
            r=(R-1)//2
        if not L==R and not (Lflag or Rflag):
            l=(l-1)//2
        while l>0:
            yield l
            l=(l-1)//2
        yield 0

    def lazyUpdate(self,*index):
        for i in reversed(index):
            v=self.lazyTree[i]
            if not v==0:
                self.lazyTree[2*i+1]+=v
                self.segTree[2*i+1]+=v
                self.lazyTree[2*i+2]+=v
                self.segTree[2*i+2]+=v
                self.lazyTree[i]=0

    def add_query(self,p,q,x):
        *index,=self.lazyIndex(p,q)
        self.lazyUpdate(*index)
        p+=self.offset
        q+=self.offset

        while p<=q:
            #q%2==1
            if q&1:
                self.lazyTree[q]+=x
                self.segTree[q]+=x
            #p%2==0
            if not p&1:
                self.lazyTree[p]+=x
                self.segTree[p]+=x
            p=p//2
            q=(q-2)//2

    def find_query(self,i):
        self.lazyUpdate(*self.lazyIndex(i,i))
        i+=self.offset
        return self.segTree[i]

    def show(self):
        print("####")
        for a in self.segTree:
            if a==INF:
                print(" ",end=" ")
            else:
                print(a,end=" ")
        print("\n####")
        for a in self.lazyTree:
            if a==0:
                print(" ",end=" ")
            else:
                print(a,end=" ")
        print("\n####")
        print()

n,q=map(int,input().split())
ST=SegmentTree(n)
for i in range(q):
    qry=list(map(int,input().split()))
    if qry[0]==0:
        ST.add_query(qry[1]-1,qry[2]-1,qry[3])
    else:
        print(ST.find_query(qry[1]-1))
