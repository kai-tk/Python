"""
Segment-Tree
    add_query(i,x):i番目にxを足す
    sum_query(p,q):[p,q]の範囲の合計
"""
class SegmentTree():
    def __init__(self,n):
        self.offset=self.setOffset(n)
        self.segTree=[0]*(2*self.offset+1)

    def setOffset(self,n):
        if n==1:
            return 1
        else:
            return 2**(n-1).bit_length()-1

    def add_query(self,i,x):
        i+=self.offset
        self.segTree[i]+=x
        while i:
            i=(i-1)//2
            self.segTree[i]+=x

    def sum_query(self,p,q):
        p+=self.offset
        q+=self.offset
        segsum=0

        while q>=p:
            #p%2==0
            if not p&1:
                segsum+=self.segTree[p]
            #q%2==1
            if q&1:
                segsum+=self.segTree[q]
            p=p//2
            q=(q-2)//2

        return segsum

    def show(self):
        print(self.segTree)

n,q=map(int,input().split())
ST=SegmentTree(n)
for i in range(q):
    qry=list(map(int,input().split()))
    #0-index
    if qry[0]==0:
        ST.add_query(qry[1]-1,qry[2])
    else:
        print(ST.sum_query(qry[1]-1,qry[2]-1))
