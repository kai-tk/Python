from collections import deque
ans=[]

n,l=map(int,input().split())
A=list(map(int,input().split()))
q=deque()

for i,a in enumerate(A):
    while q and a<=q[-1][1]:
        q.pop()
    q.append((i,a))
    if i<l-1:
        continue
    ans.append(q[0][1])
    if q and q[0][0]<=i+1-l:
        q.popleft()

print(*ans,sep=" ")
