"""
Segment-Tree
    update_query(i,x):i番目をxに変更
    min_query(p,q):[p,q]を最小値
"""
INF=(1<<31)-1

class SegmentTree():
    def __init__(self,n):
        self.offset=self.setOffset(n)
        self.segTree=[INF]*(2*self.offset+1)

    def setOffset(self,n):
        if n==1:
            return 1
        else:
            return 2**(n-1).bit_length()-1

    def update_query(self,i,x):
        i+=self.offset
        self.segTree[i]=x
        while i:
            i=(i-1)//2
            self.segTree[i]=min(self.segTree[2*i+1],self.segTree[2*i+2])

    def min_query(self,p,q):
        p+=self.offset
        q+=self.offset
        segmin=INF

        while q-p>1:
            #p%2==0
            if not p&1:
                segmin=min(segmin,self.segTree[p])
            #q%2==1
            if q&1:
                segmin=min(segmin,self.segTree[q])
            p=p//2
            q=(q-2)//2

        if p==q:
            return min(segmin,self.segTree[p])
        else:
            return min(min(segmin,self.segTree[p]),self.segTree[q])

    def show(self):
        print(self.segTree)

n,q=map(int,input().split())
ST=SegmentTree(n)
for i in range(q):
    qry=list(map(int,input().split()))
    if qry[0]==0:
        ST.update_query(qry[1],qry[2])
    else:
        print(ST.min_query(qry[1],qry[2]))
