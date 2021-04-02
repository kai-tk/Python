"""
Segment-Tree
    update_query(p,q,x):[p,q]をxに変更
    sum_query(p,q):[p,q]の合計
"""

class SegmentTree():
    def __init__(self,n):
        self.offset=self.setOffset(n)
        self.segTree=[0]*(2*self.offset+1)
        self.lazyTree=[None]*(2*self.offset+1)

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
            if not v is None:
                self.lazyTree[2*i+1]=self.segTree[2*i+1]=v//2
                self.lazyTree[2*i+2]=self.segTree[2*i+2]=v//2
                self.lazyTree[i]=None

    def update_query(self,p,q,x):
        *index,=self.lazyIndex(p,q)
        self.lazyUpdate(*index)
        p+=self.offset
        q+=self.offset
        n=1

        while p<=q:
            if q&1:
                self.lazyTree[q]=self.segTree[q]=x*n
            if not p&1:
                self.lazyTree[p]=self.segTree[p]=x*n
            p=p//2
            q=(q-2)//2
            n*=2
        for i in index:
            self.segTree[i]=self.segTree[2*i+1]+self.segTree[2*i+2]

    def sum_query(self,p,q):
        self.lazyUpdate(*self.lazyIndex(p,q))
        p+=self.offset
        q+=self.offset
        segsum=0

        while q>=p:
            if not p&1:
                segsum+=self.segTree[p]
            if q&1:
                segsum+=self.segTree[q]
            p=p//2
            q=(q-2)//2
        return segsum

    def show(self):
        print("####")
        for a in self.segTree:
            if a==0:
                print(" ",end=" ")
            else:
                print(a,end=" ")
        print("\n####")
        for a in self.lazyTree:
            if a==None:
                print(" ",end=" ")
            else:
                print(a,end=" ")
        print("\n####")
        print()

n,q=map(int,input().split())
ST=SegmentTree(n)
ans=[]
for i in range(q):
    qry=list(map(int,input().split()))
    if qry[0]==0:
        ST.update_query(qry[1],qry[2],qry[3])
    else:
        ans.append(ST.sum_query(qry[1],qry[2]))
print(*ans,sep='\n')
