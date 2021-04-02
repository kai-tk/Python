"""
1~Kを全て含む最小の区間
"""

from collections import defaultdict

n,k=map(int,input().split())
a=list(map(int,input().split()))
count=defaultdict(int)
left=0
right=0
K=0
INF=(1<<31)-1
ans=INF

for left in range(n):
    while right<n and K<k:
        if a[right]<=k and count[a[right]]==0:
            K+=1
        count[a[right]]+=1
        right+=1
    if(K<k):
        break
    ans=min(ans,right-left)
    if a[left]<=k and count[a[left]]==1:
        K-=1
    count[a[left]]-=1
    if(left==right):
        right+=1

if ans==INF:
    ans=0
print(ans)
